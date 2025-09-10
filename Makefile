# Fritz IP Updater Makefile

.PHONY: run install clean help venv

# Default Python interpreter - use .venv if it exists, otherwise system python3
VENV_DIR := .venv
PYTHON := $(if $(wildcard $(VENV_DIR)/bin/python),$(VENV_DIR)/bin/python,python3)
REQUIREMENTS := requirements.txt

# Default target
help:
	@echo "Available commands:"
	@echo "  run       - Run the Fritz IP updater application"
	@echo "  install   - Install dependencies"
	@echo "  install-requirements - Install dependencies from requirements.txt"
	@echo "  venv      - Create virtual environment only"
	@echo "  clean     - Remove virtual environment and cache files"
	@echo "  help      - Show this help message"

# Run the application
run:
	$(PYTHON) main.py

# Install dependencies (assumes requirements.txt exists or will be created)
install:
	$(if $(wildcard $(VENV_DIR)/bin/pip),$(VENV_DIR)/bin/pip,pip) install -r requirements.txt

# Create virtual environment
venv:
	python3 -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)/"
	@echo "Activate it with: source $(VENV_DIR)/bin/activate"

# Clean up
clean:
	rm -rf $(VENV_DIR)
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf .pytest_cache
	@echo "Cleanup complete"

# Create requirements.txt
requirements:
	pip freeze > $(REQUIREMENTS)
	@echo "Requirements saved to $(REQUIREMENTS)"