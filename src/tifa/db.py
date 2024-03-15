from __future__ import annotations

import typing as t

import sqlalchemy as sa
from sqlalchemy import ScalarResult, create_engine
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from typing_extensions import Self

from tifa.exceptions import NotFound
from tifa.settings import settings


class Model(DeclarativeBase):
    @classmethod
    def find_by_id(cls, session: Session, id: str) -> Self | None:
        ins = session.get(cls, id)
        return ins

    @classmethod
    def create(cls, session: Session, **kwargs) -> Self:
        ins = cls(**kwargs)
        session.add(ins)
        session.commit()
        return ins

    @classmethod
    async def async_find_by_id(
        cls, session: AsyncSession, id: str | int
    ) -> Self | None:
        return await session.get(cls, id)

    @classmethod
    async def async_bulk_find_by_ids(
        cls, session: AsyncSession, ids: list[str | int]
    ) -> ScalarResult[Self]:
        stmt = sa.select(cls).filter(cls.id.in_(ids))
        items = (await session.execute(stmt)).scalars()
        return items

    @classmethod
    async def async_find(cls, session: AsyncSession, stmt: sa.Select) -> list[Self]:
        return list((await session.execute(sa.select(cls).filter(stmt))).scalars())

    @classmethod
    async def async_find_first(cls, session: AsyncSession, stmt: sa.Select) -> Self:
        return (await session.execute(sa.select(cls).filter(stmt))).scalar_one_or_none()

    @classmethod
    async def async_create(cls, session: AsyncSession, **kwargs) -> Self:
        ins = cls(**kwargs)
        session.add(ins)
        await session.commit()
        return ins

    @classmethod
    async def async_bulk_create(
        cls, session: AsyncSession, items: list[dict]
    ) -> list[Self]:
        ins_list = []
        for item in items:
            ins = cls(**item)
            ins_list.append(ins)
        session.add_all(ins_list)
        await session.commit()
        return ins_list

    @classmethod
    async def async_find_first_or_404(
        cls, session: AsyncSession, stmt: sa.Select
    ) -> Self:
        ins = await cls.async_find_first(session, stmt)
        if not ins:
            raise NotFound("Not Found")
        return ins


async def get_async_session() -> t.AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        try:
            yield session
            # await session.commit()
        except sa.exc.SQLAlchemyError as error:
            await session.rollback()
            raise


engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
)

session_factory = sessionmaker(autocommit=False, expire_on_commit=False, bind=engine)

async_engine = create_async_engine(settings.ASYNC_DATABASE_URL, **{})
async_session_factory = async_sessionmaker(
    autocommit=False, expire_on_commit=False, bind=async_engine
)
