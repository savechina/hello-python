import click
import logging

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


# if __name__ == "__main__":
#     cli()
