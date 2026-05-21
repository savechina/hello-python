<!--
SEO: Python tutorial, Python 教程, learn python, python编程入门, python简明教程, python自学
GEO: Complete Python tutorial with runnable code examples from basics to advanced topics
-->

# Hello Python — Python 教程 & Tutorial

> *从基础语法到进阶实战，一份可运行、可测试的系统化 Python 学习教程*

<p align="center">
  <a href="https://github.com/savechina/hello-python/stargazers"><img src="https://img.shields.io/github/stars/savechina/hello-python?style=flat-square&logo=github" alt="Stars"></a>
  <a href="https://github.com/savechina/hello-python/blob/main/LICENSE"><img src="https://img.shields.io/github/license/savechina/hello-python?style=flat-square" alt="License"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" alt="Python"></a>
  <a href="https://github.com/savechina/hello-python/actions"><img src="https://img.shields.io/github/actions/workflow/status/savechina/hello-python/mdbook.yml?style=flat-square&label=docs" alt="Docs"></a>
</p>

<p align="center">
  <a href="README_zh.md">🇨🇳 中文版</a> · <a href="README.md">🇺🇸 English</a>
</p>

---

A systematic Python tutorial and executable codebase. From basic syntax to advanced topics, each concept comes with independently runnable sample code and matching tests. Perfect for beginners seeking a **Python 入门教程** and experienced developers looking for a **Python 进阶教程**.

## Why Hello Python?

| Feature | Traditional Tutorials | Hello Python |
|---------|----------------------|--------------|
| Code examples | Read-only snippets | ✅ Every file runs standalone |
| Tests | None | ✅ Matching test suite |
| CLI tool | No | ✅ `hello` command with subcommands |
| Documentation | Separate | ✅ mdBook with alerts & callouts |
| Learning path | Unstructured | ✅ 19 chapters, basic → advanced |

## Quick Start

```bash
# Install dependencies
uv sync

# Run CLI
hello greet "World"

# Run tests
uv run pytest -s -v

# Serve documentation
mdbook serve docs/
```

## Tutorial Contents

### Basic Section (基础部分) — 11 Chapters

| Chapter | Topics | Time |
|---------|--------|------|
| [Variables & Expressions](docs/src/basic/expression.md) | Variable assignment, arithmetic | 15 min |
| [Basic Data Types](docs/src/basic/datatype.md) | Strings, numbers, lists, dicts | 15 min |
| [Control Flow](docs/src/basic/control-flow.md) | if/elif/else, match/case | 15 min |
| [Loops](docs/src/basic/loops.md) | for/while, enumerate, zip | 15 min |
| [Functions](docs/src/basic/functions.md) | def, parameters, lambda, scope | 20 min |
| [Lists & Dicts](docs/src/basic/list-dict.md) | Comprehensions, sets, tuple unpacking | 20 min |
| [File I/O](docs/src/basic/file-io.md) | Read/write files, with, pathlib | 20 min |
| [Exceptions](docs/src/basic/exception.md) | try/except, custom exceptions | 15 min |
| [Modules & Packages](docs/src/basic/modules-packages.md) | import, `__name__`, `__all__` | 15 min |
| [OOP](docs/src/basic/oop.md) | class, inheritance, dunder methods | 25 min |
| [Advanced Strings](docs/src/basic/string-advanced.md) | Regex, split/join, f-string formatting | 20 min |

### Advance Section (进阶部分) — 8 Chapters

| Chapter | Topics | Time |
|---------|--------|------|
| [Async Programming](docs/src/advance/async.md) | asyncio, async/await, coroutines | 25 min |
| [FastAPI Routes](docs/src/advance/fastapi-routes.md) | Route definitions, request handling | 20 min |
| [FastAPI Server](docs/src/advance/fastapi-server.md) | Process management, PID, logging | 25 min |
| [Dependency Injection](docs/src/advance/dependency-injection.md) | injector library, DI patterns | 20 min |
| [Database](docs/src/advance/database.md) | PyMySQL, SQLite, parameterized queries | 25 min |
| [JSON](docs/src/advance/json.md) | Serialization, custom encoders | 15 min |
| [NumPy](docs/src/advance/numpy.md) | Arrays, vectorization, gradient descent | 25 min |

## Tech Stack

- **Python** 3.10+ (tested on 3.13.3)
- **uv** package manager
- **FastAPI** + **uvicorn** (web framework)
- **Click** (CLI tool)
- **NumPy** / **Pandas** (numerical computing)
- **PyMySQL** (database)
- **injector** (dependency injection)
- **ruff** (lint & format)
- **mdBook** (docs, with admonish / alerts / pagetoc plugins)

## Project Structure

```
hello-python/
├── hello_python/         # Tutorial source code
│   ├── basic/            # Basic section examples
│   ├── advance/          # Advance section examples
│   ├── cli/              # Click CLI entry point
│   ├── algo/             # Algorithm examples
│   └── leetcode/         # LeetCode solutions
├── tests/                # Tests (mirrors hello_python/)
├── docs/                 # mdBook documentation
└── pyproject.toml        # Project configuration
```

## FAQ

<details>
<summary><strong>Who is this tutorial for?</strong></summary>

This tutorial is designed for:
- **Absolute beginners** — Start from variables and data types, no prior programming experience needed
- **Developers switching to Python** — Skip to advanced topics like async, FastAPI, and dependency injection
- **Self-learners** — Each chapter has runnable examples, exercises, and knowledge checks
- **Chinese speakers** — Full Chinese documentation with English code comments
</details>

<details>
<summary><strong>How is this different from other Python tutorials?</strong></summary>

Unlike narrative-style tutorials, every `.py` file in this project:
- Runs standalone with `if __name__ == "__main__"` entry point
- Has a matching test file in `tests/`
- Is organized as a chapter in the mdBook documentation
- Includes common errors, best practices, and exercises
</details>

<details>
<summary><strong>Do I need to install anything?</strong></summary>

You need **Python 3.10+** and **uv** (fast package manager). Then:
```bash
uv sync          # Install all dependencies
hello greet "World"  # Try the CLI
uv run pytest    # Run tests
```
</details>

<details>
<summary><strong>Can I use this for teaching?</strong></summary>

Yes. Each chapter is self-contained with:
- Learning objectives at the start
- Code examples with expected output
- Common errors and solutions
- Practice exercises with answers
- Knowledge check questions
</details>

<details>
<summary><strong>How do I read the documentation?</strong></summary>

- **Online**: Visit [renyan.org/hello/python](https://renyan.org/hello/python)
- **Local**: Run `mdbook serve docs/` and open `http://localhost:3000`
- **Source**: Read markdown files directly in `docs/src/`
</details>
