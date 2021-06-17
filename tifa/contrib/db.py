from __future__ import annotations

import typing as t
from contextvars import ContextVar

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker, as_declarative

from tifa.settings import get_settings

_session: ContextVar[t.Optional[AsyncSession]] = ContextVar("_session", default=None)


class SQLAlchemy:
    Model: t.Type[BaseModel]
    Session: sessionmaker

    def __init__(self):
        self.Model = BaseModel
        self.engine = self.create_engine()
        self.Session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    def create_engine(self):
        return create_async_engine(
            get_settings().POSTGRES_DATABASE_URI,
            echo=True,
        )

    def create_all(self, connection):
        return self.Model.metadata.create_all(bind=connection)

    def drop_all(self, connection):
        return self.Model.metadata.drop_all(bind=connection)

    @property
    def session(self) -> AsyncSession:
        """Return an instance of Session local to the current async context."""
        session = _session.get()
        if session is None:
            session = self.Session()
            _session.set(session)
        return session


def _fetch_local_session():
    from tifa.globals import db
    return db.session


@as_declarative()
class BaseModel:
    __mapper_args__ = {"eager_defaults": True}

    # @declared_attr
    # def __tablename__(cls):
    #     return cls.__name__.lower()

    @classmethod
    async def add(cls, **kwargs) -> BaseModel:
        obj = cls(**kwargs)
        session = _fetch_local_session()
        session.add(obj)
        return obj

    @classmethod
    async def all(cls, **kwargs) -> list[BaseModel]:
        session = _fetch_local_session()
        return (await session.execute(select(cls).where(**kwargs))).scalars().all()
