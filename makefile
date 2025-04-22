.PHONY: test coverage

test:
	python3 -m unittest discover -s tests -p "test_*.py"

coverage:
	coverage run -m unittest discover -s tests -p "test_*.py"
	coverage report -m
	coverage html
