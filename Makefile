.PHONY: test coverage

# Run unit tests with detailed output
test:
	python -m unittest discover -s tests -p "test_*.py" -v

# Run unit tests and report test coverage
coverage:
	coverage run -m unittest discover -s tests -p "test_*.py"
	coverage report
	coverage html  # Optional: To generate an HTML report for viewing
