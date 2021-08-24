import os
import pathlib
import types
import warnings
from typing import Optional

from pydantic import BaseSettings

ROOT = pathlib.Path(__file__).parent.absolute()


class GlobalSetting(BaseSettings):
    TITLE: str = "Tifa"
    DESCRIPTION: str = "Yet another opinionated fastapi-start-kit with best practice"

    TEMPLATE_PATH: str = f"{ROOT}/templates"

    STATIC_PATH: str = "/static"
    STATIC_DIR: str = f"{ROOT}/static"

    SENTRY_DSN: Optional[str]

    DEBUG: bool = False
    ENV: str = "LOCAL"
    SECRET_KEY: str = "change me"

    POSTGRES_DATABASE_URI: str = "postgresql://tifa:tifa123@postgres:5432/tifa"
    KAFKA_BOOTSTRAP_SERVERS: str = "http://kafka:9091"
    KAFKA_TOPIC: str = "tifa.pg_to_es"
    REDIS_CACHE_URI: str = "redis"
    WHITEBOARD_URI: str = "redis://redis:6379/1"
    REDIS_CELERY_URL: str = "redis://redis:6379/1"


def from_pyfile(filename: str) -> GlobalSetting:
    filename = os.path.join(ROOT, filename)
    d = types.ModuleType("conf")
    d.__file__ = filename
    try:
        with open(filename, mode="rb") as config_file:
            exec(compile(config_file.read(), filename, "exec"), d.__dict__)
    except OSError as e:
        e.strerror = f"Unable to load configuration file ({e.strerror})"
        raise
    if hasattr(d, "Setting"):
        return d.Setting()
    else:
        warnings.warn("You May Forgot Setting, Use GlobalSettings")
        return GlobalSetting()


if "SETTING_PATH" not in os.environ:
    warnings.warn("You May Forgot ENV SETTING_PATH, Use GlobalSettings")
    setting = GlobalSetting()
else:
    setting = from_pyfile(os.environ["SETTING_PATH"])
