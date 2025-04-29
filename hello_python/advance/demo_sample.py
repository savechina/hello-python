import signal
import click
import uvicorn
import threading
import os
import sys
import time
import psutil
from fastapi import FastAPI

# FastAPI 应用
app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello, FastAPI!"}


# 配置
APP_NAME = "fastapi_app"
PID_FILE = f"{APP_NAME}.pid"
LOG_FILE = f"{APP_NAME}.log"
CONFIG = {"app": app, "host": "0.0.0.0", "port": 8000}
WORKING_DIR = "."  # 替换为项目目录

# 全局变量
server = None
running = False


def run_server():
    """运行 uvicorn 服务器"""
    global server, running
    server = uvicorn.Server(uvicorn.Config(**CONFIG))
    running = True
    with open(LOG_FILE, "a") as log:
        sys.stdout = log
        sys.stderr = log
        server.run()
    running = False


def check_pid():
    """检查 PID 文件和进程状态"""
    if not os.path.exists(PID_FILE):
        return None
    with open(PID_FILE, "r") as f:
        pid = int(f.read().strip())
    if psutil.pid_exists(pid):
        return pid
    os.remove(PID_FILE)
    return None


def signal_handler(sig, frame):
    """处理终止信号"""
    click.echo("Received termination signal")
    stop()


@click.group()
def cli():
    """Manage FastAPI service"""


@cli.command()
def start():
    """Start FastAPI service"""
    if pid := check_pid():
        click.echo(f"{APP_NAME} already running with PID {pid}")
        sys.exit(1)

    click.echo(f"Starting {APP_NAME}...")
    os.chdir(WORKING_DIR)
    worker = threading.Thread(target=run_server, daemon=True)
    worker.start()

    pid = os.getpid()
    with open(PID_FILE, "w") as f:
        f.write(str(pid))
    time.sleep(5)
    if running:
        click.echo(f"{APP_NAME} started with PID {pid}")
        # 捕获信号并保持主进程运行
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        while running:
            time.sleep(1)
    else:
        click.echo(f"Failed to start. Check {LOG_FILE}")
        sys.exit(1)


@cli.command()
def stop():
    """Stop FastAPI service"""
    if not (pid := check_pid()):
        click.echo(f"{APP_NAME} not running")
        sys.exit(1)

    click.echo(f"Stopping {APP_NAME} (PID {pid})...")
    global running, server
    running = False
    if server:
        server.should_exit = True
    os.kill(pid, os.name == "nt" and 9 or 15)  # SIGTERM (15) for Unix, 9 for Windows
    time.sleep(1)
    if psutil.pid_exists(pid):
        click.echo(f"Force stopping...")
        os.kill(pid, 9)  # SIGKILL
    os.remove(PID_FILE)
    click.echo(f"{APP_NAME} stopped")


@cli.command()
def status():
    """Check FastAPI service status"""
    if pid := check_pid():
        click.echo(f"{APP_NAME} running with PID {pid}")
    else:
        click.echo(f"{APP_NAME} not running")


@cli.command()
def restart():
    """Restart FastAPI service"""
    stop()
    time.sleep(1)
    start()


if __name__ == "__main__":
    cli()
