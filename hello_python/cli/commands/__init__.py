"""
Commands Module define all command and  dynamically load and register to click main command
"""

import importlib
import os


def get_commands():
    commands = []
    # Define the directory where your command modules are located
    command_dir = os.path.dirname(os.path.abspath(__file__))
    # Iterate over all the files in the directory
    for filename in os.listdir(command_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            # Import the module and get the command object
            module_name = f"hello_python.cli.commands.{filename[:-3]}"
            module = importlib.import_module(module_name)
            command = getattr(module, filename[:-3])
            commands.append(command)
    return commands
