from __future__ import annotations

from typing import Optional

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleSpanProcessor, BatchSpanProcessor,
)

from sqlalchemy.future import select
from sqlalchemy.orm import as_declarative

from tifa.contrib.db import SQLAlchemy
from tifa.contrib.globals import glb

g = glb


@as_declarative()
class BaseModel:
    __mapper_args__ = {"eager_defaults": True}

    # @declared_attr
    # def __tablename__(cls):
    #     return cls.__name__.lower()

    @classmethod
    async def add(cls, **kwargs) -> BaseModel:
        obj = cls(**kwargs)
        db.session.add(obj)
        return obj

    @classmethod
    async def all(cls, **kwargs) -> list[BaseModel]:
        return (await db.session.execute(select(cls).where(**kwargs))).scalars().all()

    @classmethod
    async def get(cls, id) -> Optional[BaseModel]:
        return await db.session.get(cls, id)


db = SQLAlchemy(BaseModel)

tracer = trace.get_tracer(__name__)

jaeger_exporter = JaegerExporter(
    agent_host_name='jaeger',
    agent_port=6831,
)

span_processor = BatchSpanProcessor(jaeger_exporter)

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create(
            {
                SERVICE_NAME: "tifa"
            }
        )
    )
)
provider = trace.get_tracer_provider()
provider.add_span_processor(span_processor)
