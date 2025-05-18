# Makefile for ml-jobs-analysis project

.PHONY: run test format lint clean

# Run the main script
run:
	python src/main.py

# Run all unit tests
test:
	python -m unittest discover -s test

# Format code using black
format:
	black .

# Lint using flake8
lint:
	flake8 .

# Clean Python cache
clean:
	find . -type d -name "__pycache__" -exec rm -r {} + || true
	find . -type f -name "*.pyc" -delete || true
