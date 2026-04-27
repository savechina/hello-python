# FastAPI 服务器管理 (FastAPI Server)

## 导语

在生产环境中，一个 Web 应用不仅要能启动和运行，还要能优雅地处理信号、管理进程、记录日志、支持热重载和关闭。FastAPI 的基础路由让你能定义 API，但如何像真正的服务一样管理它——启动、停止、重启、PID 文件管理——这才是生产级开发的关键技能。

## 学习目标

- 学会使用 ServiceManager 模式管理 FastAPI 服务
- 掌握 PID 文件管理和进程信号处理
- 了解 uvicorn 的生产配置和后台运行

## 概念介绍

`fastapi_server_sample.py`（332 行）展示了一个完整的生产级服务器管理模式：
- **ServiceManager 类**：封装了 FastAPI 应用的生命周期管理
- **PID 文件**：记录进程 ID，用于后续的查询和终止
- **信号处理**：响应 `SIGTERM`/`SIGINT` 优雅关闭
- **日志管理**：将 stdout/stderr 重定向到日志文件

这种模式在微服务架构中很常见——服务需要可管理、可监控、可重启。

## 代码示例

### 示例 1：ServiceManager 类

```python
class ServiceManager:
    """管理 FastAPI/Uvicorn 服务的类。"""
    
    def __init__(self, app_name, config):
        self.app_name = app_name
        self.config = config
        self.pid_file = f"{app_name}.pid"
        self.log_file = f"{app_name}.log"
    
    def start(self):
        """启动服务并记录 PID"""
        # ... uvicorn.run() 配置
        pid = os.getpid()
        with open(self.pid_file, "w") as f:
            f.write(str(pid))
        print(f"Started {self.app_name} with PID {pid}")
```

### 示例 2：进程管理

```python
def stop(self):
    """通过读取 PID 文件终止服务"""
    pid = self._read_pid()
    if pid:
        os.kill(pid, signal.SIGTERM)
        self._remove_pid()
        print(f"Stopped {self.app_name} (PID {pid})")

def _read_pid(self):
    """读取保存的 PID"""
    if os.path.exists(self.pid_file):
        with open(self.pid_file) as f:
            return int(f.read().strip())
    return None
```

### 示例 3：信号处理

```python
import signal
import sys

def _signal_handler(self, signum, frame):
    print(f"Received signal {signum}")
    self._cleanup()
    sys.exit(0)

def start(self):
    # 注册信号处理器
    signal.signal(signal.SIGTERM, self._signal_handler)
    signal.signal(signal.SIGINT, self._signal_handler)
    # 启动 uvicorn...
```

> [!NOTE]
> 信号处理确保服务器接收到 `kill` 命令时能优雅关闭连接，不会丢失正在处理的请求。

## 常见错误与解决

> [!WARNING]
> **错误 1：PID 文件残留导致无法启动**
>
> 服务器异常退出后 PID 文件还存在，下次启动时检查到"服务正在运行"。
>
> **解决**：启动时先检查 PID 文件中的进程是否真的存在（`os.kill(pid, 0)` 测试）。

> [!WARNING]
> **错误 2：`uvicorn.run()` 阻塞主线程**
>
> `uvicorn.run()` 是阻塞调用，会阻塞主线程，导致后续代码无法执行。
>
> **解决**：使用 `target` 参数 + 线程，或用 `subprocess` 在子进程中启动。

## 最佳实践

1. **始终使用 PID 文件** 管理服务进程生命周期
2. **注册信号处理** 确保优雅关闭（graceful shutdown）
3. **日志输出到文件** 而非 stdout（生产环境中 stdout 不可靠）

## 练习

1. 写一个函数，检查 PID 文件中保存的进程是否真的存在。

<details>
<summary>查看答案</summary>

```python
import os

def is_running(pid):
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True

pid = int(open("service.pid").read())
print(f"Service running: {is_running(pid)}")
```

</details>

2. 用 `subprocess` 启动一个 uvicorn 服务器（不阻塞主进程）。

<details>
<summary>查看答案</summary>

```python
import subprocess

# 非阻塞启动
process = subprocess.Popen(
    ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"],
    stdout=open("server.log", "a"),
    stderr=subprocess.STDOUT,
)
print(f"Server started with PID: {process.pid}")
```

</details>

## 知识检查

1. PID 文件的主要作用是？
   - A. 记录服务器日志
   - B. 记录进程 ID 用于后续管理
   - C. 配置服务器端口
   - D. 存储环境变量

2. `signal.SIGTERM` 信号的含义是？
   - A. 强制终止进程（无法捕获）
   - B. 请求终止进程（可捕获和处理）
   - C. 暂停进程
   - D. 恢复进程

3. `os.kill(pid, 0)` 的作用是？
   - A. 终止指定的进程
   - B. 向进程发送空信号
   - C. 检查进程是否存在，不实际发送信号
   - D. 修改进程优先级

<details>
<summary>查看答案</summary>

1. B — PID 文件记录进程 ID，用于 stop/restart 操作
2. B — SIGTERM 是可捕获的终止请求（`kill` 默认发送）
3. C — `signal 0` 是一个特殊的"检查存在"信号

</details>

## 本章小结

- ServiceManager 封装了服务的完整生命周期
- PID 文件是管理服务进程的关键工具
- 信号处理（SIGTERM/SIGINT）确保优雅关闭
- `os.kill(pid, 0)` 可以检查进程是否存在
- `uvicorn.run()` 是阻塞调用，需要线程/subprocess 管理
- 日志输出应重定向到文件

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| daemon | 守护进程 | 在后台持续运行提供服务 |
| PID file | PID 文件 | 记录进程 ID 的文件 |
| signal handling | 信号处理 | 捕获和处理操作系统信号 |
| graceful shutdown | 优雅关闭 | 在完成当前请求后关闭 |
| ASGI server | ASGI 服务器 | 运行 ASGI 应用的服务器 |

## 下一步

- [依赖注入](./dependency-injection.md) → 学会使用 injector 管理依赖关系

## 源码链接

- [fastapi_server_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/advance/fastapi_server_sample.py)
