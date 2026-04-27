# PROJECT KNOWLEDGE BASE

**Generated:** 2026-04-26
**Commit:** 4e460a5
**Branch:** main

## OVERVIEW
Python tutorial/code library (hello-python). Learning resource covering basic → advanced Python concepts, with a Click-based CLI and FastAPI examples. Uses `uv` package manager, Python 3.13. Includes mdBook-based documentation.

## STRUCTURE
```
hello-python/
├── hello_python/         # Main package (tutorial modules)
│   ├── basic/            # Python basics: datatypes, expressions
│   ├── advance/          # Advanced: async, FastAPI, DI, numpy, DB
│   ├── cli/              # Click CLI entry point + commands
│   ├── algo/             # Algorithm examples
│   ├── leetcode/         # LeetCode solutions
│   └── utils/            # Shared utilities
├── tests/                # Test suite (mirrors hello_python/)
│   ├── basic/            # Tests for basic/ modules
│   ├── advance/          # Tests for advance/ modules
│   └── cli/              # CLI tests
├── docs/                 # mdBook documentation (SUMMARY.md, chapter_1.md)
├── bin/                  # Scripts (entry point wrapper)
├── data/                 # Sample data files (gitignored)
├── scripts/              # Utility scripts
└── examples/             # Standalone examples
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Add basic Python topic | `hello_python/basic/` | Mirror in `tests/basic/` |
| Add advanced topic (async, web, DI) | `hello_python/advance/` | Largest module, 9 files |
| Add CLI subcommand | `hello_python/cli/commands/` | Filename MUST match variable name |
| Add algorithm | `hello_python/algo/` | Single-file modules |
| Add LeetCode solution | `hello_python/leetcode/` | Single-file modules |
| Write documentation | `docs/src/` | mdBook chapters |
| Tests | `tests/` mirrors `hello_python/` | unittest.TestCase-based |

## CONVENTIONS
- Module naming: `<topic>_sample.py` pattern used in advance/ and basic/
- Test classes: `Test<Feature>Sample` (not standard `Test<Feature>`)
- Dynamic CLI command loading: `hello_python/cli/commands/__init__.py` scans directory, imports modules, registers commands
- Entry point: `hello = hello_python.cli:main` (pyproject.toml `[project.scripts]`)
- No `__main__.py` — must use `hello` CLI command, not `python -m hello_python`
- Empty `__init__.py` files in subpackages — no re-exports, imports via full paths

## ANTI-PATTERNS (THIS PROJECT)
- Bare `except Exception: pass` in some test files (silent failure)
- Tests without assertions (print-only verification)
- No `pytest.mark.parametrize` — manual test duplication
- No conftest.py — no shared test fixtures
- CLI dynamic loader assumes `filename[:-3] == variable_name` convention (fragile)
- `filename` typos in test class names (e.g., `TestExpressioneSample` — note extra 'e')

## UNIQUE STYLES
- **Dual-purpose codebase**: Both runnable tutorials AND testable module
- Each sample file is executable standalone (`if __name__ == "__main__"` blocks)
- `Makefile` uses `uv run` for all commands (no virtualenv activation needed)
- FastAPI server example with async + APScheduler scheduler demo
- Uses `injector` for DI — uncommon in Python, demonstrates advanced patterns

## COMMANDS
```bash
# Install dependencies
uv sync

# Run CLI
hello greet "World"
hello user "Alice"

# Test
uv run pytest -s -v
uv run pytest tests/basic/  # Run specific subset

# Lint & Format
uv run ruff check .
uv run ruff format .

# Build
uv build

# Make shortcuts (all wrap uv)
make test    # pytest -s -v
make lint    # ruff check .
make format  # ruff format .
make build   # uv build
make install # uv sync

# Run mdBook docs
mdbook serve docs/
```

## NOTES
- Python 3.13.3 (bleeding edge, check compatibility for some packages)
- `data/` directory is gitignored — sample data not committed
- Largest file: `hello_python/advance/fastapi_server_sample.py` (332 lines)
- Constitution in `.specify/memory/constitution.md` v2.0.0 — 8 principles, Python-focused
- CI: GitHub Actions with pytest, ruff, mdbook workflows
- No pre-commit hooks configured

## Active Technologies
- Python 3.10+ (per pyproject.toml `requires-python`); tested with Python 3.13.3 + mdBook 0.4.52+ (with admonish, alerts, pagetoc plugins), Click 8.1+ (CLI) (001-python-basic-tutorial)
- N/A — documentation-only feature, no persistent data (001-python-basic-tutorial)
- Python 3.10+ (per pyproject.toml `requires-python`); tested with Python 3.13.3 + mdBook 0.4.52+ (with admonish, alerts, pagetoc plugins), Click 8.1+, FastAPI, asyncio, PyMySQL, injector, NumPy (001-python-basic-tutorial)

## Recent Changes
- 001-python-basic-tutorial: Added Python 3.10+ (per pyproject.toml `requires-python`); tested with Python 3.13.3 + mdBook 0.4.52+ (with admonish, alerts, pagetoc plugins), Click 8.1+ (CLI)
