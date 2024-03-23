from __future__ import annotations

import typing as t

from loguru import logger
from pydantic import BaseModel
from tortoise import fields, Tortoise, connections
from tortoise.expressions import Q
from tortoise.models import Model as TTModel

from tifa.settings import tortoise_config


class Model(TTModel):
    class Meta:
        abstract = True

    id = fields.BigIntField(pk=True)

    @classmethod
    def find_first(cls, *args: Q, **kwargs: t.Any) -> t.Self:
        return cls.filter(*args, **kwargs).first()

    def __str__(self):
        return f"{self.__class__.__name__}-#{self.id}"


def setup_db_models(app):
    logger.info("setup db models")

    @app.on_event("startup")
    async def init_orm() -> None:
        await db_hook_on_startup()

    @app.on_event("shutdown")
    async def close_orm() -> None:  # pylint: disable=W0612
        await db_hook_on_shutdown()


async def db_hook_on_startup():
    await Tortoise.init(config=tortoise_config)
    logger.info("Tortoise-ORM started")


async def db_hook_on_shutdown():
    await connections.close_all()
    logger.info("Tortoise-ORM shutdown")
