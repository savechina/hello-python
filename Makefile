.PHONY: help install test clean lint format build
# Variables
POETRY = poetry
PYTHON = $(POETRY) run python
TEST = $(POETRY) run pytest

#Targets
help: 
	@echo "Available make tasks:"
	@echo "  install    - Install dependencies"
	@echo "  test       - Run tests"
	@echo "  clean      - Clean up build artifacts"
	@echo "  lint       - Lint the code"
	@echo "  format     - Format the code"
	@echo "  build      - Build the project"

install:
	@echo "Installing dependencies..."
	$(POETRY) install

# test:
# 	$(POETRY) run pytest

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__ .pytest_cache .mypy_cache .coverage dist
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "__pycache__" -exec rm -rf {} +
lint:
	$(POETRY) run pylint .

format:
	@echo "Formating ..."
	$(POETRY) run black .

build:
	@echo "Building ..."
	$(POETRY) build

test:
	@echo "Running tests..."
	$(POETRY) run python -m unittest discover -s tests