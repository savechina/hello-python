.PHONY: help init install sync run test clean lint format build

# Variables
UV ?= uv
UV_RUN = $(UV) run
PYTHON = $(UV_RUN) python
TEST = $(UV_RUN) pytest

# Targets
help:
	@echo "Available make tasks:"
	@echo "  init       - Install uv (via Homebrew)"
	@echo "  install    - Install/sync dependencies (uv sync)"
	@echo "  sync       - Alias for install"
	@echo "  run        - Run the CLI (make run ARGS='greet World')"
	@echo "  test       - Run tests"
	@echo "  clean      - Clean up build artifacts"
	@echo "  lint       - Lint the code"
	@echo "  format     - Format the code"
	@echo "  build      - Build sdist + wheel (uv build)"

init:
	@echo "Initializing project..."
	brew install uv

install:
	@echo "Installing dependencies..."
	$(UV) sync

sync: install

run:
	@echo "Running hello CLI..."
	$(UV_RUN) hello $(ARGS)

test:
	@echo "Running tests..."
	$(UV_RUN) pytest -s -v

clean:
	@echo "Cleaning up..."
	rm -rf build dist .pytest_cache .mypy_cache .ruff_cache .coverage
	find . -maxdepth 1 -name "*.log" -type f -delete
	find . -path ./.venv -prune -o -name "*.pyc" -exec rm -f {} +
	find . -path ./.venv -prune -o -name "__pycache__" -type d -exec rm -rf {} +

lint:
	$(UV_RUN) ruff check .

format:
	@echo "Formatting ..."
	$(UV_RUN) ruff format .

build:
	@echo "Building ..."
	$(UV) build
