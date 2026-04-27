"""
File I/O Sample.
Demonstrates open(), context manager, read/write modes, and pathlib.
"""

import tempfile
from pathlib import Path


def open_read_write_sample():
    """Demonstrates basic file operations with open()."""
    # Write to a temp file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("Hello, Python!\n")
        f.write("你好，世界！\n")
        filepath = f.name

    # Read back
    with open(filepath, "r") as f:
        content = f.read()
        print(f"file content:\n{content}")

    # Append mode
    with open(filepath, "a") as f:
        f.write("Appended line.\n")

    with open(filepath, "r") as f:
        print(f"after append:\n{f.read()}")


def context_manager_sample():
    """Demonstrates context manager (with statement) for automatic resource cleanup."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
        filepath = f.name

    # Reading line by line
    with open(filepath, "r") as f:
        for line in f:
            print(f"line: {line.strip()}")


def pathlib_sample():
    """Demonstrates pathlib.Path for modern file system operations."""
    path = Path(".")

    # Check if directory exists
    print(f"current dir exists: {path.exists()}")

    # List Python files
    py_files = [p.name for p in path.iterdir() if p.name.endswith(".py")]
    print(f"Python files in current dir: {py_files}")

    # Get file info
    readme = path / "README.md"
    if readme.exists():
        print(f"README.md size: {readme.stat().st_size} bytes")


if __name__ == "__main__":
    open_read_write_sample()
    print("---")
    context_manager_sample()
    print("---")
    pathlib_sample()
