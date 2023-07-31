import os
import pathlib
from pathlib import Path
from typing import Optional

import dj_database_url
import dotenv
import warnings

from pydantic import BaseSettings

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

    SENTRY_DSN: Optional[str]

    DEBUG: bool = False
    ENV: str = "LOCAL"
    SECRET_KEY: str = "change me"

    DATABASE_URL: str = "postgresql://tifa:tifa%26123@postgres:5432/tifa"
    REDIS_CACHE_URI: str = "redis://localhost:6379"
    REDIS_CELERY_URL: str = "redis://redis:6379/6"
    WHITEBOARD_URI: str = "redis://redis:6379/1"

    class Config:
        env_file = APP_SETTINGS


settings = GlobalSetting()

"""
django settings, only orm and cache
"""


SECRET_KEY = settings.SECRET_KEY
DEBUG = False
INSTALLED_APPS = [
    "tifa",
    "django.contrib.postgres"
]

MIDDLEWARE = []
ROOT_URLCONF = "tifa.asgi.urls"

TEMPLATES = []

WSGI_APPLICATION = "tifa.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATABASES = {
    "default": dj_database_url.config(
        default=settings.DATABASE_URL,
        conn_max_age=600,
    ),
}

DATABASES["default"]["OPTIONS"] = {}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": settings.REDIS_CACHE_URI
    }
}

TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
LOGGING = {}
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
# CELERY_RESULT_BACKEND = "django-db"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TRACK_STARTED = True
CELERYD_HIJACK_ROOT_LOGGER = False
