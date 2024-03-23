# Tifa

Yet another **opinionated** fastapi-start-kit with best practice

![tifa](https://user-images.githubusercontent.com/5625783/118087406-19244200-b3f8-11eb-839d-f8faf3044f2d.gif)

for my goddess -- Tifa

## Feature

1. Async! Async! Async!
	- async web framework by fastapi
	- async orm tortoise orm
	- htmx && tailwind && alpinejs
2. Much Less History Burden
	- newer sdk
	- newer python (3.11+)
	- newer docker compose way for developing experience
3. Best Practice
	- try automate every boring stuff with makefile/docker
	- embeded ipython repl for fast debugging and code prototype
	- type hint
	- build with poetry

## Quick Setup

```bash
poetry install
# build local docker image
make build-tifa
# make start
make debug
```

## Credits

0. saleor
1. https://github.com/ryanwang520/create-flask-skeleton
2. https://github.com/tiangolo/full-stack-fastapi-postgresql

