from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings, PostgresDsn

import pathlib

ROOT = pathlib.Path(__file__).parent.absolute()


class BasicSettings(BaseSettings):
    TITLE: str = "Tifa Lockhart"
    DESCRIPTION: str = "Yet another opinionated fastapi-start-kit with best practice"
    API_V1_ROUTE: str = "/api/v1"
    OPED_API_ROUTE: str = "/api/v1/openapi.json"

    TEMPLATE_PATH: str = f"{ROOT}/templates"

    STATIC_PATH: str = "/static"
    STATIC_DIR: str = f"{ROOT}/static"

    SENTRY_DSN: Optional[str]

    DEBUG: bool = False
    ENV: str = "LOCAL"

    POSTGRES_DATABASE_URI: str = "postgresql+asyncpg://tifa:tifa123@localhost:5432/tifa"
    KAFKA_BOOTSTRAP_SERVERS: str = "http://localhost:9091"
    KAFKA_TOPIC: str = "tifa.message"
    REDIS_CACHE_URI: str = "redis"
    WHITEBOARD_URI: str = "redis://localhost/1"


class TestSettings(BasicSettings):
    POSTGRES_DATABASE_URI: str = (
        "postgresql+asyncpg://tifa:tifa123@localhost:5432/tifa_test"
    )


class ProdSettings(BasicSettings):
    POSTGRES_DATABASE_URI: str = "postgresql+asyncpg://tifa:tifa123@localhost:5432/tifa"


test_settings = TestSettings()
prod_settings = ProdSettings()


def get_settings(env: str = None) -> BasicSettings:
    if env == "test":
        return test_settings
    return prod_settings
