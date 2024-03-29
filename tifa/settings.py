import os
import pathlib
import warnings
from typing import Optional

from pydantic_settings import BaseSettings

ROOT = pathlib.Path(__file__).parent.absolute()

APP_SETTINGS = os.environ.get("APP_SETTINGS")
if not APP_SETTINGS:
    warnings.warn("!!!未指定APP_SETTINGS!!!, 极有可能运行错误")


class GlobalSetting(BaseSettings):
    TITLE: str = "Tifa"
    DESCRIPTION: str = "Yet another opinionated fastapi-start-kit with best practice"

    TEMPLATE_PATH: str = f"{ROOT}/templates"

    STATIC_PATH: str = "/static"
    STATIC_DIR: str = f"{ROOT}/static"

    # SENTRY_DSN: Optional[str]

    DEBUG: bool = False
    ENV: str = "LOCAL"
    SECRET_KEY: str = "change me"
    SENTRY_DSN: Optional[str] = ""

    ASYNC_DATABASE_URL: str = "mysql://root:@mysql:3306/tifa?charset=utf8mb4"
    REDIS_CACHE_URI: str = "redis://localhost:6379"
    REDIS_CELERY_URL: str = "redis://redis:6379/6"


settings = GlobalSetting(_env_file=APP_SETTINGS)

tortoise_config = {
    "connections": {"default": settings.ASYNC_DATABASE_URL},
    "apps": {
        "models": {
            "models": ["tifa.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
