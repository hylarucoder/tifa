.PHONY:  help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-30s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

start: ## start
	uvicorn tifa.app:current_app --reload

flake8: ## lint
	poetry run flake8 tifa

publish: ## publish package to pypi
	poetry publish --build

test: ## test
	python -m pytest tests

format: ## publish package to pypi
	black tifa
	black tests

dbinit:
	alembic init -t async ./migration
