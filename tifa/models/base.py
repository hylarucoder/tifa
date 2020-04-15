from __future__ import annotations
import sqlalchemy as sa

from tifa.globals import db


class BaseModel:
    created_at = sa.Column(
        sa.DateTime,
    )
    updated_at = sa.Column(
        sa.DateTime,
    )

    @classmethod
    async def create(cls, **kwargs) -> BaseModel:
        obj = cls(**kwargs)
        return obj

    @classmethod
    async def all(cls, **kwargs) -> list[BaseModel]:
        return obj
