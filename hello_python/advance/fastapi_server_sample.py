import os
import sys
import signal
import time
import threading
import logging
from typing import Optional

import click
import psutil
import uvicorn
from fastapi import FastAPI

# --- FastAPI 应用定义 ---
# (保持不变或根据您的应用进行修改)
app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello, FastAPI!"}


# --- 服务管理类 ---


class ServiceManager:
    """
    管理 FastAPI/Uvicorn 服务的类。

    封装了启动、停止、重启、状态检查、PID 文件管理和日志重定向的逻辑。
    """

    def __init__(
        self,
        app_instance: FastAPI,
        app_name: str = "fastapi_app",
        host: str = "0.0.0.0",
        port: int = 8000,
        working_dir: str = ".",
        log_level: str = "info",
    ):
        """
        初始化服务管理器。

        Args:
            app_instance: 要运行的 FastAPI 应用实例。
            app_name: 服务名称，用于生成 PID 和日志文件名。
            host: Uvicorn 监听的主机。
            port: Uvicorn 监听的端口。
            working_dir: 运行服务的工作目录。
            log_level: Uvicorn 的日志级别。
        """
        self.app = app_instance
        self.app_name = app_name
        self.host = host
        self.port = port
        self.working_dir = os.path.abspath(working_dir)  # 确保是绝对路径
        self.log_level = log_level

        self.pid_file = os.path.join(self.working_dir, f"{self.app_name}.pid")
        self.log_file = os.path.join(self.working_dir, f"{self.app_name}.log")

        self.uvicorn_config = uvicorn.Config(
            app=self.app,
            host=self.host,
            port=self.port,
            log_level=self.log_level,
            # 添加其他需要的 Uvicorn 配置, 例如:
            # reload=True, # 开发时使用
            # workers=4,   # 生产环境使用
        )
        self._server: Optional[uvicorn.Server] = None
        self._server_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()  # 用于优雅停止的事件

        # 配置日志记录器 (可选, Uvicorn 也有自己的日志)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filename=self.log_file,
            filemode="a",
        )
        self.logger = logging.getLogger(__name__)

    def _write_pid(self):
        """将当前进程 PID 写入 PID 文件。"""
        pid = os.getpid()
        try:
            with open(self.pid_file, "w") as f:
                f.write(str(pid))
            self.logger.info(f"PID {pid} written to {self.pid_file}")
        except IOError as e:
            self.logger.error(f"Failed to write PID file {self.pid_file}: {e}")
            sys.exit(1)  # 无法写入 PID 文件是严重错误

    def _remove_pid(self):
        """安全地移除 PID 文件。"""
        if os.path.exists(self.pid_file):
            try:
                os.remove(self.pid_file)
                self.logger.info(f"PID file {self.pid_file} removed.")
            except OSError as e:
                self.logger.error(f"Error removing PID file {self.pid_file}: {e}")

    def _get_pid_from_file(self) -> Optional[int]:
        """从 PID 文件读取并验证 PID。"""
        if not os.path.exists(self.pid_file):
            return None
        try:
            with open(self.pid_file, "r") as f:
                pid_str = f.read().strip()
                if not pid_str:
                    return None
                pid = int(pid_str)
            # 验证 PID 是否真实存在并且与服务相关 (基本检查)
            if psutil.pid_exists(pid):
                # 可选: 更严格的检查, 如检查进程名称或命令行
                # try:
                #     proc = psutil.Process(pid)
                #     if self.app_name in proc.name() or any(self.app_name in part for part in proc.cmdline()):
                #         return pid
                # except (psutil.NoSuchProcess, psutil.AccessDenied):
                #     pass # 进程不存在或无权访问
                return pid  # 基本检查通过
            else:
                # PID 文件存在但进程已死, 清理 PID 文件
                self.logger.warning(
                    f"Process with PID {pid} not found, removing stale PID file."
                )
                self._remove_pid()
                return None
        except ValueError:
            self.logger.error(f"Invalid PID found in {self.pid_file}. Removing.")
            self._remove_pid()
            return None
        except IOError as e:
            self.logger.error(f"Error reading PID file {self.pid_file}: {e}")
            return None

    def _run_server(self):
        """在单独的线程中运行 Uvicorn 服务器。"""
        # 重定向该线程的标准输出/错误到日志文件
        # 注意: 这可能不会捕获 Uvicorn 所有的内部日志，Uvicorn 自己的日志配置更可靠
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        try:
            with open(self.log_file, "a") as log:
                sys.stdout = log
                sys.stderr = log
                self._server = uvicorn.Server(config=self.uvicorn_config)
                self.logger.info(f"Uvicorn server starting ({self.host}:{self.port})")
                self._server.run()  # 这个调用会阻塞直到服务器停止
                self.logger.info("Uvicorn server stopped.")
        except Exception as e:
            self.logger.exception(
                f"Error running Uvicorn server: {e}"
            )  # 使用 exception 记录堆栈跟踪
        finally:
            sys.stdout = original_stdout  # 恢复标准输出/错误
            sys.stderr = original_stderr
            self._server = None  # 标记服务器实例已停止
            self._stop_event.set()  # 通知主线程服务器已停止

    def _signal_handler(self, sig, frame):
        """处理 SIGINT 和 SIGTERM 信号。"""
        self.logger.warning(f"Received signal {sig}. Initiating graceful shutdown...")
        self.stop()
        sys.exit(0)  # 确保在处理信号后退出

    def start(self):
        """启动 FastAPI 服务作为后台进程。"""
        if pid := self._get_pid_from_file():
            click.echo(f"{self.app_name} is already running with PID {pid}.")
            sys.exit(1)

        click.echo(f"Starting {self.app_name}...")
        self.logger.info(f"Changing working directory to {self.working_dir}")
        try:
            os.chdir(self.working_dir)
        except OSError as e:
            self.logger.error(f"Failed to change directory to {self.working_dir}: {e}")
            click.echo(
                f"Error: Could not change directory to {self.working_dir}. Aborting.",
                err=True,
            )
            sys.exit(1)

        # 清理停止事件，以防上次未完全清理
        self._stop_event.clear()

        # 启动 Uvicorn 服务器线程
        # 使用 non-daemon 线程，以便主线程可以等待它
        self._server_thread = threading.Thread(
            target=self._run_server, name=f"{self.app_name}Worker"
        )
        self._server_thread.start()

        # 短暂等待，检查服务器是否启动成功 (可以改进为更可靠的检查)
        time.sleep(3)  # 等待服务器初始化

        # 检查线程是否仍在运行，并且 _server 实例是否已创建 (表示 run() 被调用)
        if self._server_thread.is_alive() and self._server:
            self._write_pid()  # 只有在服务器看似成功启动后才写入 PID
            click.echo(f"{self.app_name} started successfully with PID {os.getpid()}.")
            self.logger.info(
                f"{self.app_name} started with PID {os.getpid()}. Main process monitoring."
            )

            # 设置信号处理，现在由主进程处理
            signal.signal(signal.SIGINT, self._signal_handler)
            signal.signal(signal.SIGTERM, self._signal_handler)

            # 主线程现在等待服务器停止事件或线程结束
            # 这样主进程会保持运行，直到 stop() 被调用或服务器意外退出
            self._stop_event.wait()  # 等待 _run_server 完成或 stop() 被调用设置事件

            self.logger.info("Main process detected server stop event. Exiting.")
            # 服务器停止后清理 PID 文件
            self._remove_pid()

        else:
            self.logger.error(
                "Server thread did not start correctly or exited prematurely."
            )
            click.echo(
                f"Error: Failed to start {self.app_name}. Check logs at {self.log_file}",
                err=True,
            )
            # 尝试清理可能残留的线程
            if self._server_thread and self._server_thread.is_alive():
                # 尝试给 Uvicorn 发送停止信号（如果 server 实例存在）
                if self._server:
                    self._server.should_exit = True
                self._server_thread.join(timeout=5)  # 等待线程退出
            self._remove_pid()  # 清理可能意外写入的 PID
            sys.exit(1)

    def stop(self, force: bool = False):
        """停止 FastAPI 服务。"""
        pid = self._get_pid_from_file()
        if not pid:
            click.echo(f"{self.app_name} is not running.")
            # 确保没有孤立的PID文件
            self._remove_pid()
            return  # 如果没有运行，则无需执行任何操作

        click.echo(f"Stopping {self.app_name} (PID {pid})...")
        self.logger.info(f"Attempting to stop process with PID {pid}")

        try:
            proc = psutil.Process(pid)
            # 首先尝试发送 SIGTERM (标准终止信号)
            self.logger.info(f"Sending SIGTERM to process {pid}")
            proc.terminate()  # 等同于 os.kill(pid, signal.SIGTERM)

            # 等待进程终止
            try:
                proc.wait(timeout=10)  # 等待最多 10 秒
                self.logger.info(f"Process {pid} terminated gracefully.")
                click.echo(f"{self.app_name} stopped.")
            except psutil.TimeoutExpired:
                self.logger.warning(
                    f"Process {pid} did not terminate after SIGTERM. Trying SIGKILL."
                )
                click.echo("Process did not stop gracefully, forcing kill...")
                proc.kill()  # 等同于 os.kill(pid, signal.SIGKILL)
                proc.wait(timeout=5)  # 等待 SIGKILL 生效
                self.logger.info(f"Process {pid} killed.")
                click.echo(f"{self.app_name} stopped forcefully.")

        except psutil.NoSuchProcess:
            self.logger.warning(
                f"Process with PID {pid} not found during stop sequence."
            )
            click.echo(f"{self.app_name} process (PID {pid}) already gone.")
        except psutil.AccessDenied:
            self.logger.error(f"Permission denied to stop process {pid}.")
            click.echo(f"Error: Permission denied to stop process {pid}.", err=True)
            # 即使无法终止进程，也应尝试清理 PID 文件，因为服务状态未知
        except Exception as e:
            self.logger.error(f"An unexpected error occurred during stop: {e}")
            click.echo(f"An error occurred: {e}", err=True)
        finally:
            # 无论停止是否成功，都清理 PID 文件
            # 如果进程被强制杀死或意外消失，stop_event 可能不会被设置
            # 这里强制设置，以防主线程卡住（如果 stop 是从外部调用的）
            self._stop_event.set()
            self._remove_pid()
            # 确保线程资源被释放（如果线程还在）
            if self._server_thread and self._server_thread.is_alive():
                self._server_thread.join(timeout=1)

    def restart(self):
        """重启 FastAPI 服务。"""
        click.echo(f"Restarting {self.app_name}...")
        if self._get_pid_from_file():
            self.stop()
            time.sleep(2)  # 等待端口释放等
        else:
            click.echo(f"{self.app_name} was not running. Starting it now.")
        self.start()  # stop 会清理 PID, start 会重新创建

    def status(self):
        """检查 FastAPI 服务状态。"""
        if pid := self._get_pid_from_file():
            try:
                proc = psutil.Process(pid)
                # 获取更详细的状态
                status_info = proc.status()
                cpu_percent = proc.cpu_percent(interval=0.1)
                memory_info = proc.memory_info()
                click.echo(f"{self.app_name} is running:")
                click.echo(f"  PID: {pid}")
                click.echo(f"  Status: {status_info}")
                click.echo(f"  CPU Usage: {cpu_percent:.2f}%")
                click.echo(
                    f"  Memory Usage: {memory_info.rss / (1024 * 1024):.2f} MB (RSS)"
                )
                click.echo(f"  Working Directory: {self.working_dir}")
                click.echo(f"  Log File: {self.log_file}")
            except psutil.NoSuchProcess:
                click.echo(
                    f"{self.app_name} (PID {pid} from file) is not running. Stale PID file cleaned."
                )
                self._remove_pid()  # 清理无效的 PID 文件
            except psutil.AccessDenied:
                click.echo(
                    f"{self.app_name} is running with PID {pid}, but details cannot be accessed (permission denied)."
                )
        else:
            click.echo(f"{self.app_name} is not running.")
