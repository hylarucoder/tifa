from __future__ import annotations

from celery import Celery

from tifa.settings import settings

# pytest no need to check
if not settings.ENV == "TEST":
    use_console_exporter = True

celery = Celery()
celery.conf.broker_url = settings.REDIS_CELERY_URL
celery.conf.timezone = "Asia/Shanghai"
