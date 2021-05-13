# Tifa

Yet another **opinionated** fastapi-start-kit with best practice

![](./docs/images/tifa.gif)

for my goddess -- Tifa

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

