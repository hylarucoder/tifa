from __future__ import annotations

from typing import TypeVar

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from tifa.contrib.globals import glb
from tifa.settings import settings

T = TypeVar('T')


class SQLAlchemy:
    Model: T
    AsyncSession: sessionmaker
    Session: sessionmaker

    def __init__(self, Model: T):
        self.g = glb
        self.Model = Model
        self.engine = self.create_engine()
        self.AsyncSession = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)  # type: ignore
        self.Session = sessionmaker(self.engine, autocommit=False, autoflush=False, )  # type: ignore

    def create_engine(self):
        return create_engine(
            settings.POSTGRES_DATABASE_URI,
            echo=True,
        )

    def create_async_engine(self):
        return create_async_engine(
            settings.POSTGRES_DATABASE_URI,
            echo=True,
        )

    def create_all(self, connection):
        return self.Model.metadata.create_all(bind=connection)

    def drop_all(self, connection):
        return self.Model.metadata.drop_all(bind=connection)

    @property
    def async_session(self) -> AsyncSession:
        if not self.g.async_session:
            self.g.async_session = self.AsyncSession()
        return self.g.async_session

    @property
    def session(self) -> Session:
        if not self.g.session:
            self.g.session = self.Session()
        return self.g.session
