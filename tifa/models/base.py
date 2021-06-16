from __future__ import annotations
import sqlalchemy as sa

from tifa.globals import db


class BaseModelMixin:
    created_at = sa.Column(
        sa.DateTime,
    )
    updated_at = sa.Column(
        sa.DateTime,
    )

    @classmethod
    async def create(cls, **kwargs) -> BaseModelMixin:
        obj = cls(**kwargs)  # type: ignore
        return obj

    @classmethod
    async def all(cls, **kwargs) -> list[BaseModelMixin]:
        return []
