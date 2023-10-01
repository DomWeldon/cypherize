help:
	@echo "Usage:"
	@echo "    make help             prints this help."
	@echo "    make docs             build and serve model schema docs."
	@echo "    make fix              fix formatting and import sort ordering."
	@echo "    make format           run the format checker (black)."
	@echo "    make lint             run the linter (flake8)."
	@echo "    make repl             open a bpython repl."
	@echo "    make setup            set up/update the local dev env."
	@echo "    make sort             run the sort checker (isort)."
	@echo "    make test             run the test suite."
	@echo "    make check 					 run mypy check"


.PHONY: docs-auto
docs-auto:
	pdm run sphinx-apidoc -o docs/source/API cypherize -f --module-first --no-headings

.PHONY: docs-build
docs-build:
	pdm run sphinx-build docs/source docs/build

.PHONY: docs-serve
docs-serve:
	pdm run python -m http.server 8001 --directory=docs/build

docs: docs-auto docs-build browser-project-docs docs-serve

.PHONY: fix
fix:
	pdm run black cypherize tests
	pdm run isort .

.PHONY: format
format:
	@echo "Running black" && pdm run black --check cypherize tests || exit 1

.PHONE: check
check:
	@echo "Running Type Checks using MyPy" && pdm run mypy . || exit 1

.PHONY: lint
lint:
	@echo "Running flake8" && pdm run flake8 app || exit 1

.PHONY: repl
repl:
	pdm run bpython

.PHONY: setup
setup:
	poetry install
	direnv allow
	pdm run pre-commit install

.PHONY: browser-api-docs
browser-api-docs:
	pdm run python -m webbrowser "http://localhost:8000/docs"

.PHONY: browser-project-docs
browser-project-docs:
	pdm run python -m webbrowser "http://localhost:8001"

init: \
	setup \
	docs-auto \
	docs-build \
	browser-api-docs

.PHONY: sort
sort:
	@echo "Running Isort" && pdm run isort . -c || exit 1

.PHONY: test
test:
	pdm run py.test tests

.PHONY: jotter
jotter:
	pdm run python jotter.py
