from __future__ import annotations

import re
import typing as t
import sqlalchemy as sa

from celery import Celery
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import as_declarative, declared_attr, Session

from tifa.contrib.db import SQLAlchemy
from tifa.exceptions import ApiException, NotFound
from tifa.settings import settings


def camel_to_snake_case(name):
    name = re.sub(r"((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))", r"_\1", name)
    return name.lower().lstrip("_")


T = t.TypeVar("T", bound="BaseModel")


@as_declarative()
class BaseModel:
    id = sa.Column(sa.Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return camel_to_snake_case(cls.__name__)

    @property
    def class_name(self) -> str:
        """Shortcut for returning class name."""
        return self.__class__.__name__


DT = t.TypeVar("DT")


class Dal:
    session: Session

    def __init__(self, s=None):
        if not s:
            self.session = session
        else:
            self.session = s

    """
    更通用
    """

    def execute_all(self, stmt, unique=False) -> list:
        """
        stmt = select(User).join(Address).where(Address.email == 'e@sa.us')
        # when using joinedload() against collections, use unique() on the result
        users = session.execute(
            select(User).options(joinedload(User.addresses)).order_by(User.id)
        ).unique().all()
        """
        if unique:
            return self.session.execute(stmt).scalars().all()
        else:
            return self.session.execute(stmt).unique().scalars().all()

    def execute_one(self, stmt) -> DT:
        """
        stmt = select(User).join(Address).where(Address.email == 'e@sa.us')
        """
        return self.session.execute(stmt).scalar_one()

    def get(self, clz: DT, id) -> t.Optional[DT]:
        return self.session.get(clz, id)

    def get_or_404(self, clz: DT, id) -> DT:
        ins = self.session.get(clz, id)
        if not ins:
            raise ApiException("not found")
        return ins

    def first_or_404(self, clz: DT, *args) -> DT:
        ins = (self.session.execute(select(clz).where(*args))).scalars().first()
        if not ins:
            raise ApiException("not found")
        return ins

    def all(self, clz: DT, **kwargs) -> list[DT]:
        return self.execute_all(select(clz).where(**kwargs))

    def add(self, clz: DT, **kwargs) -> DT:
        obj = clz(**kwargs)
        self.session.add(obj)
        return obj

    def commit(self):
        self.session.commit()


class AsyncDal:
    session: AsyncSession

    def __init__(self, s):
        self.session = s

    async def add(self, clz: DT, **kwargs) -> DT:
        obj = clz(**kwargs)
        self.session.add(obj)
        return obj

    async def all(self, clz: DT, **kwargs) -> list[DT]:
        return (await self.session.execute(select(clz).where(**kwargs))).scalars().all()

    async def get(self, clz: DT, id) -> t.Optional[DT]:
        return await self.session.get(clz, id)

    async def get_or_404(self, clz: DT, id) -> DT:
        ins = await self.session.get(clz, id)
        if not ins:
            raise NotFound(f"{clz} not found")
        return ins

    async def first_or_404(self, clz: DT, *args) -> DT:
        ins = (await self.session.execute(select(clz).where(*args))).scalars().first()
        if not ins:
            raise NotFound(f"{clz} not found")
        return ins

    async def commit(self):
        await self.session.commit()


db = SQLAlchemy(BaseModel)
# thread local session
session = db.session
# TODO: should init in request context?
async_session = db.async_session

if t.TYPE_CHECKING:

    class Model(BaseModel):  # hacking for type annotation
        ...


else:
    Model = db.Model

tracer = trace.get_tracer(__name__)

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
celery.conf.broker_url = settings.REDIS_CELERY_URL
celery.conf.timezone = "Asia/Shanghai"
