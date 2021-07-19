# Tifa

Yet another **opinionated** fastapi-start-kit with best practice

![tifa](https://user-images.githubusercontent.com/5625783/118087406-19244200-b3f8-11eb-839d-f8faf3044f2d.gif)

for my goddess -- Tifa

## Feature

1. Async! Async! Async!
	- web framework by fastapi
	- socket.io by python-socketio
	- async and sync orm supported by sqlalchemy/alembic migration
2. Much Less History Burden
	- newer sdk
	- newer python (3.9+)
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
make build-elasticsearch
# make start
make debug
```

## issues

### 01 grpc cannot be installed on apple silicon

```
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export CFLAGS="-I/opt/homebrew/opt/openssl/include"
export LDFLAGS="-L/opt/homebrew/opt/openssl/lib"
```

## Credits

1. https://github.com/ryanwang520/create-flask-skeleton
2. https://github.com/tiangolo/full-stack-fastapi-postgresql

