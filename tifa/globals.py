from __future__ import annotations
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleSpanProcessor,
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


db = SQLAlchemy(BaseModel)

trace.set_tracer_provider(TracerProvider())
provider = trace.get_tracer_provider()
provider.add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter("tifa"))
)
tracer = trace.get_tracer(__name__)
