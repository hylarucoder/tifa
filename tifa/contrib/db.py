from __future__ import annotations

import datetime
import decimal
import json
from asyncio import current_task
from typing import TypeVar, Type

import orjson
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_scoped_session,
)
from sqlalchemy.orm import sessionmaker, Session, scoped_session

from tifa.conf import setting

T = TypeVar("T")


def default(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    # if isinstance(obj, datetime.date):
    #     return str(obj)
    # if isinstance(obj, datetime.datetime):
    #     return str(obj)
    # if isinstance(obj, datetime.time):
    #     return str(obj)
    raise TypeError


def json_serializer(d: dict):
    return orjson.dumps(d).decode()


class SQLAlchemy:
    Model: T
    session: Session
    async_session: AsyncSession
    AsyncSession: Type[AsyncSession]

    def __init__(self, Model: T):
        self.Model = Model
        engine = create_engine(
            setting.POSTGRES_DATABASE_URI,
            echo=True,
        )
        self.engine = engine
        session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.session = scoped_session(session_factory)  # type: ignore
        async_engine = create_async_engine(
            setting.POSTGRES_DATABASE_URI_ASYNC,
            future=True,
            echo=True,
            json_serializer=json_serializer,
        )
        self.AsyncSession = async_session_factory = sessionmaker(  # type: ignore
            async_engine, expire_on_commit=False, class_=AsyncSession
        )
        self.async_session = async_scoped_session(  # type: ignore
            async_session_factory, scopefunc=current_task
        )

    def create_all(self, connection):
        return self.Model.metadata.create_all(bind=connection)

    def drop_all(self, connection):
        return self.Model.metadata.drop_all(bind=connection)
