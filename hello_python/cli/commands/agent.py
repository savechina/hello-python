import click


@click.group()
def agent():
    """Commands related to Agent."""
    pass


@agent.command()
@click.argument("agent_name")
def create(agent_name):
    """Create a new agent."""
    click.echo(f"Project {agent_name} created.")


@agent.command()
@click.argument("agent_name")
def delete(agent_name):
    """Delete an existing agent."""
    click.echo(f"Project {agent_name} deleted.")


@agent.command()
@click.argument("agent_name")
def start(agent_name):
    """Start an existing agent."""
    click.echo(f"Start {agent_name} started.")
