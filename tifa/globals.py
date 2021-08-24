from __future__ import annotations

import typing as t

from celery import Celery
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

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

tracer = trace.get_tracer(__name__)

use_console_exporter = True

if use_console_exporter:
    span_processor = BatchSpanProcessor(ConsoleSpanExporter())
else:
    jaeger_exporter = JaegerExporter(
        agent_host_name="jaeger",
        agent_port=6831,
    )

    span_processor = BatchSpanProcessor(jaeger_exporter)

trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({SERVICE_NAME: "tifa"}))
)
provider = trace.get_tracer_provider()
provider.add_span_processor(span_processor)

celery = Celery()
celery.conf.broker_url = setting.REDIS_CELERY_URL
celery.conf.timezone = "Asia/Shanghai"
