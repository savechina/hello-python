import click
from fastapi import FastAPI

from hello_python.advance.fastapi_server_sample import ServiceManager, app

# --- Click 命令行接口 ---


@click.group()
def fastapi():
    """A command-line tool to manage the FastAPI service."""
    pass


# 在这里实例化管理器，传入 FastAPI 应用实例和配置
service_manager = ServiceManager(
    app_instance=app, app_name="my_fastapi_service", port=8080
)


@fastapi.command()
def start():
    """Starts the FastAPI service."""
    service_manager.start()


@fastapi.command()
@click.option(
    "--force", is_flag=True, help="Force kill the process if graceful stop fails."
)
def stop(force):
    """Stops the FastAPI service."""
    # 注意: 当前 stop 实现内部处理了强制逻辑，但保留 force 标志可能未来有用
    service_manager.stop(force=force)  # force 参数目前未在 stop 内部严格使用


@fastapi.command()
def restart():
    """Restarts the FastAPI service."""
    service_manager.restart()


@fastapi.command()
def status():
    """Checks the status of the FastAPI service."""
    service_manager.status()
