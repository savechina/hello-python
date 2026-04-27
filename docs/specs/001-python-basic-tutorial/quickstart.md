# Quickstart: Hello Python Basic Tutorial

## Prerequisites

- Python 3.10+ (3.13.3 recommended)
- `uv` package manager installed
- mdBook 0.4.52+ with plugins (`mdbook-admonish`, `mdbook-alerts`, `mdbook-pagetoc`)
- Git

## Setup (5 minutes)

```bash
# 1. Install Python dependencies
uv sync

# 2. Verify Python version
python --version  # Should be 3.13.x

# 3. Install mdBook plugins (one-time setup)
# Copy plugins from hello-rust or install via cargo:
cp -r ../hello-rust/docs/src/assets/css/admonish.css docs/src/assets/css/mdbook-admonish.css
cp -r ../hello-rust/docs/theme/pagetoc.css docs/theme/
cp -r ../hello-rust/docs/theme/pagetoc.js docs/theme/

# 4. Update book.toml with plugin config (see research.md for exact config)

# 5. Build documentation
mdbook build docs

# 6. Serve documentation locally
mdbook serve docs --open

# Documentation will be available at http://localhost:3000
```

## Run Tutorial Code Samples

```bash
# Run any sample file directly
python -m hello_python.basic.datatype_sample
python -m hello_python.basic.expression_sample

# Or via the CLI
hello greet "Python Learner"
```

## Run Tests

```bash
# Run all basic tutorial tests
uv run pytest tests/basic/ -s -v

# Run a specific module's tests
uv run pytest tests/basic/test_datatype_sample.py -s -v
```

## Project Structure

```
docs/src/basic/          # Basic tutorial chapter markdown files
docs/src/advance/        # Advance tutorial chapter markdown files
hello_python/basic/      # Basic Python sample code
hello_python/advance/    # Advance Python sample code
tests/basic/             # Tests for basic sample code
```

## Development Workflow

1. Create `*_sample.py` in `hello_python/basic/` or use existing `hello_python/advance/`
2. Create `test_*_sample.py` in `tests/basic/` (basic only)
3. Create `topic.md` in `docs/src/basic/` or `docs/src/advance/`
4. Update `docs/src/SUMMARY.md` with new chapter link
5. Run tests: `uv run pytest tests/basic/`
6. Run lint: `uv run ruff check .`
7. Build docs: `mdbook build docs`
8. Verify locally: `mdbook serve docs`

## Advance Sample Code Notes

- `hello_python/advance/asyncs_sample.py` — Uses `apscheduler` dependency (already in `pyproject.toml`)
- `hello_python/advance/fastapi_sample.py` + `fastapi_server_sample.py` — Requires FastAPI + uvicorn (already in deps)
- `hello_python/advance/database_sample.py` — Refactored to not auto-connect; requires live MySQL for full demo
- `hello_python/advance/database_sqlite_sample.py` — Self-contained, uses in-memory SQLite, works standalone
- `hello_python/advance/injector_sample.py` — Uses `injector` library (already in deps)
- `hello_python/advance/numpy_sample.py` — Uses `numpy` (already in deps)
- `hello_python/advance/json_sample.py` — Standard library only, works standalone
