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

flake8: ## lint
	poetry run flake8 tifa

publish: ## publish package to pypi
	poetry publish --build

test: ## test
	docker compose run --rm tifa-toolbox bash -c "python -m pytest tests"

format: ## publish package to pypi
	black tifa
	black tests

dbinit:
	docker compose run --rm tifa-toolbox bash -c "alembic init -t async ./migration"

docker-build: ## build and compose up
	docker compose build && docker-compose up

docker-build-no-cache: ## build --no-cache
	docker compose build --no-cache  && docker-compose up

before-up: ## some deamons
	docker compose up -d redis postgres elasticsearch jaeger

start: ## runserver
	make before-up
	docker compose stop tifa-web
	docker compose up --no-deps tifa-web

beat: ## beat
	docker compose up tifa-beat

worker: ## worker
	docker compose up tifa-worker

tifa-monitor: ## flower
	docker compose up tifa-monitor

# docker images

build-tifa: ## > tifa
	docker build -t 'tifa:local' -f 'compose/app/Dockerfile' .

build-tifa-no-cache: ## > tifa
	docker build -t 'tifa:local' -f 'compose/app/Dockerfile' --no-cache .

build-elasticsearch: ## > elasticsearch
	docker build -t 'elasticsearch:local' -f 'compose/elasticsearch/Dockerfile' .

build-elasticsearch-no-cache: ## > elasticsearch
	docker build -t 'elasticsearch:local' -f 'compose/elasticsearch/Dockerfile' . --no-cache
