"""
Tutorial commands: run sample code by category and topic.
Usage:
    hello basic            # List all basic topics
    hello basic datatype   # Run datatype sample
    hello advance          # List all advance topics
    hello advance async    # Run async sample
"""

import click
import importlib
import importlib.util
import pkgutil
import runpy
import ast
import os



def get_module_docstring(module_path):
    """Extract module docstring without executing the file."""
    try:
        with open(module_path, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        docstring = ast.get_docstring(tree)
        return (docstring or "No description").strip().split("\n")[0]
    except Exception:
        return "No description"


def list_topics(category):
    """List all available topics in a category."""
    package = importlib.import_module(f"hello_python.{category}")
    topics = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        if modname.endswith("_sample") and not ispkg:
            topic = modname.replace("_sample", "")
            file_path = os.path.join(os.path.dirname(package.__file__), f"{modname}.py")
            desc = get_module_docstring(file_path)
            topics.append((topic, desc))
    
    if not topics:
        click.echo(f"No topics found in {category}.")
        return

    click.echo(f"\n📚 {category.capitalize()} Topics:")
    click.echo("-" * 40)
    for topic, desc in sorted(topics):
        click.echo(f"  {topic:<20s} {desc}")
    click.echo(f"\n💡 Run: hello {category} <topic>")


def run_sample(category, topic):
    """Run a specific sample module."""
    module_name = f"hello_python.{category}.{topic}_sample"
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        click.echo(f"❌ Topic '{topic}' not found in {category}.")
        click.echo("Available topics:")
        list_topics(category)
        return

    click.echo(f"▶ Running {module_name}...\n")
    runpy.run_module(module_name, run_name="__main__")


@click.command()
@click.argument("topic", required=False)
def basic(topic):
    """Run or list basic Python tutorials."""
    if topic:
        run_sample("basic", topic)
    else:
        list_topics("basic")


@click.command()
@click.argument("topic", required=False)
def advance(topic):
    """Run or list advanced Python tutorials."""
    if topic:
        run_sample("advance", topic)
    else:
        list_topics("advance")
