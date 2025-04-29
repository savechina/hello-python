import click

from hello_python.advance import fastapi_sample

@click.group()
def agent():
    """AutoAgent an AI Agent Fast MCP Service"""
    pass



@agent.command()
def start():
    """Start FastAPI service"""
    click.echo(f"Start to start service...")
    fastapi_sample.start()

@agent.command()
def stop():
    """Stop FastAPI service"""
    click.echo(f"Start to stop service ...")
    fastapi_sample.stop()


@agent.command()
def status():
    """Check FastAPI service status"""
    click.echo(f"check service status.")
    fastapi_sample.status()

@agent.command()
def restart():
    """Restart FastAPI service"""
    fastapi_sample.restart()