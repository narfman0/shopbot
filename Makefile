default: test

clean: clean-build clean-pyc

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

init:
	pip install .

init-dev:
	pip install -r requirements_test.txt

run
	python -m shopbot.shopbot

run-test:
	pytest

release: clean
	python setup.py sdist bdist_wheel
	twine upload --repository pypi dist/*

t: run-test
test: init-dev t
