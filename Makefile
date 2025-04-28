.PHONY: help install test clean lint format build
# Variables
UV = uv
PYTHON = $(UV) run python
TEST = $(UV) run pytest

#Targets
help: 
	@echo "Available make tasks:"
	@echo "  install    - Install dependencies"
	@echo "  test       - Run tests"
	@echo "  clean      - Clean up build artifacts"
	@echo "  lint       - Lint the code"
	@echo "  format     - Format the code"
	@echo "  build      - Build the project"

init:
	@echo "Initializing project..."
	brew install uv
	
install:
	@echo "Installing dependencies..."
	$(UV) sync

test:
	@echo "Running tests..."
	$(UV) run pytest -s -v 

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__ .pytest_cache .mypy_cache .coverage dist
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "__pycache__" -exec rm -rf {} +
lint:
	$(UV) run ruff check .

format:
	@echo "Formating ..."
	$(UV) run ruff format .

build:
	@echo "Building ..."
	$(UV) build

# test:
# 	@echo "Running tests..."
# 	$(UV) run python -m unittest discover -s tests