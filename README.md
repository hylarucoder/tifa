# Tifa

Yet another **opinionated** fastapi-start-kit with best practice

![tifa](https://user-images.githubusercontent.com/5625783/118087406-19244200-b3f8-11eb-839d-f8faf3044f2d.gif)

for my goddess -- Tifa

## Feature

1. Async! Async! Async!
  - web framework by fastapi
	- socket.io by python-socketio
  - async orm by sqlalchemy/alembic migration
2. Much Less History Burden
	- newer sdk
	- newer python (3.9+)
3. Best Practice
  - Python Type Hint
  - Build With Poetry

## Quick Setup

```bash
poetry install

# db setup
createuser tifa
createdb tifa
psql -c "alter user tifa with encrypted password 'tifa123';"
psql -c "alter user tifa with superuser;"
```

## credits

1. https://github.com/ryanwang520/create-flask-skeleton
2. https://github.com/tiangolo/full-stack-fastapi-postgresql

