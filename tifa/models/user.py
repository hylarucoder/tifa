from tortoise import fields

from tifa.models.base import BaseModel


class User(BaseModel):
    id = fields.IntField(pk=True)
    nickname = fields.CharField(max_length=50)
