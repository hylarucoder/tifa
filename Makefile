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

mypy: ## mypy
	poetry run mypy tifa

publish: ## publish package to pypi
	poetry publish --build

test: ## test
	docker-compose run --rm tifa-toolbox-test bash -c "python -m pytest tests"

format: ## publish package to pypi
	black tifa
	black tests

shell_plus:
	docker-compose run --rm tifa-toolbox bash -c "tifa-cli shell_plus"

db.init:
	docker-compose run --rm tifa-toolbox bash -c "tifa-cli db init"

db.makemigrations:
	docker-compose run --rm tifa-toolbox bash -c "tifa-cli db makemigrations"

db.migrate:
	docker-compose run --rm tifa-toolbox bash -c "tifa-cli db migrate"

docker-build: ## build and compose up
	docker-compose build && docker-compose up

docker-build-no-cache: ## build --no-cache
	docker-compose build --no-cache  && docker-compose up

before-up: ## some deamons
	docker-compose up -d redis postgres

before-full-up: ## some deamons
	docker-compose up -d redis postgres

start: ## runserver
	make before-up
	docker-compose stop tifa-web
	docker-compose up --no-deps tifa-web

beat: ## beat
	docker-compose up tifa-beat

worker: ## worker
	docker-compose up tifa-worker

monitor: ## flower
	docker-compose up tifa-monitor

# docker images

build-tifa: ## > tifa
	docker build -t 'tifa:latest' -f 'compose/app/Dockerfile' .

build-tifa-no-cache: ## > tifa
	docker build -t 'tifa:latest' -f 'compose/app/Dockerfile' --no-cache .

build-elasticsearch: ## > elasticsearch
	docker build -t 'elasticsearch:local' -f 'compose/elasticsearch/Dockerfile' .

build-elasticsearch-no-cache: ## > elasticsearch
	docker build -t 'elasticsearch:local' -f 'compose/elasticsearch/Dockerfile' . --no-cache

publish-tifa-image: ## > elasticsearch
	echo ${DOCKER_PASS} | docker login -u twocucao --password-stdin
	docker pull twocucao/tifa:latest || true
	docker build -t 'tifa:latest' -f 'compose/app/Dockerfile' . --cache-from=twocucao/tifa:latest
	docker tag 'tifa:latest' twocucao/tifa:latest && docker push twocucao/tifa:latest || true


