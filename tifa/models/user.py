from __future__ import annotations

from tortoise import fields

from tifa.db import Model


class User(Model):
    class Meta:
        table = "user"

    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=50, index=True)
    password_hash = fields.CharField(max_length=200)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
