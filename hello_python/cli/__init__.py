import click
import logging
from .commands import get_commands

logger = logging.getLogger(__name__)

logger.debug("initial hello command...")


@click.group()
def cli():
    """A Hello CLI tool"""
    pass


@cli.command()
@click.argument("name")
def user(name):
    """User NAME"""
    click.echo(f"hello ,{name}")


@cli.command()
@click.argument("name")
def greet(name):
    """greet NAME"""
    logger.debug("greet command...")

    click.echo(f"Hello, {name}!")

logger.debug("dynmaically load and regester command...")
# Dynamically load and register command
for command in get_commands():
    logger.debug("register command: %s", command.name)
    cli.add_command(command)


def main():
    """Main entry point for the CLI tool."""
    cli()


# if __name__ == "__main__":
#     main()
