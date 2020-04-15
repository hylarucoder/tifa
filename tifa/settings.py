from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings, PostgresDsn

import pathlib

ROOT = pathlib.Path(__file__).parent.absolute()


class TifaSettings(BaseSettings):
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

    class Config:
        case_sensitive = True
        env_prefix = "TIFA_"


@lru_cache()
def get_settings() -> TifaSettings:
    # override if required
    return TifaSettings(_env_file=".env")
