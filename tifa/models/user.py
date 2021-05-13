from tifa.globals import db
from tifa.models.base import BaseModel
import sqlalchemy as sa


class User(db.Model, BaseModel):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True)
    nickname = sa.Column(sa.String(50))


class SysUser(db.Model, BaseModel):
    __tablename__ = "sys_user"

    id = sa.Column(sa.Integer, primary_key=True)
    nickname = sa.Column(sa.String(50))
