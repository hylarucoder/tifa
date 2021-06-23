import os
import pathlib
from typing import Optional

from pydantic import BaseSettings as BSettings

ROOT = pathlib.Path(__file__).parent.absolute()


class BaseSettings(BSettings):
    TITLE: str = "Tifa Lockhart"
    DESCRIPTION: str = "Yet another opinionated fastapi-start-kit with best practice"

    TEMPLATE_PATH: str = f"{ROOT}/templates"

    STATIC_PATH: str = "/static"
    STATIC_DIR: str = f"{ROOT}/static"

    SENTRY_DSN: Optional[str]

    DEBUG: bool = False
    ENV: str = "LOCAL"

    POSTGRES_DATABASE_URI: str = "postgresql+asyncpg://tifa:tifa123@postgres:5432/tifa"
    KAFKA_BOOTSTRAP_SERVERS: str = "http://kafka:9091"
    KAFKA_TOPIC: str = "tifa.message"
    REDIS_CACHE_URI: str = "redis"
    WHITEBOARD_URI: str = "redis://redis:6379/1"


class Settings(BSettings):
    ...


if "SETTING_PATH" not in os.environ:
    raise Exception("Must Specify Env SETTING_PATH")

# os.environ.setdefault("SETTING_PATH", "/opt/tifa/settings_docker.py")
setting_path = os.environ["SETTING_PATH"]
with open(setting_path, mode="rb") as file:
    exec(file.read())
settings = Settings()
