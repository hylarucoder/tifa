from __future__ import annotations

import typing as t

from celery import Celery

from tifa.conf import setting
from tifa.contrib.db import SQLAlchemy
from tifa.db.base import BaseModel

db = SQLAlchemy(BaseModel)
# thread local session
session = db.session

if t.TYPE_CHECKING:

    class Model(BaseModel):  # hacking for type annotation
        ...


else:
    Model = db.Model

# pytest no need to check
if not setting.ENV == "TEST":
    use_console_exporter = True

celery = Celery()
celery.conf.broker_url = setting.REDIS_CELERY_URL
celery.conf.timezone = "Asia/Shanghai"
