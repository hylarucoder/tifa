# Tifa

Yet another **opinionated** fastapi-start-kit with best practice

![](./docs/images/tifa.gif)

for my goddess -- Tifa

## Quick Setup

```
poetry install
createuser tifa
createdb tifa
psql -c "alter user tifa with encrypted password 'tifa123';"
psql -c "alter user tifa with superuser;"
# aerich init -t tifa.app.current_app.TORTOISE_ORM
```

## credits

1. https://github.com/ryanwang520/create-flask-skeleton
2. https://github.com/tiangolo/full-stack-fastapi-postgresql

