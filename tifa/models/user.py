from tifa.globals import db
from tifa.models.base import BaseModelMixin
import sqlalchemy as sa


class User(BaseModelMixin, db.Model):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True)
    nickname = sa.Column(sa.String(50))


class SysUser(BaseModelMixin, db.Model):
    __tablename__ = "sys_user"

    id = sa.Column(sa.Integer, primary_key=True)
    nickname = sa.Column(sa.String(50))
