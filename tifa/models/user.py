import sqlalchemy as sa

from tifa.globals import Model


class User(Model):
    id = sa.Column(sa.Integer, primary_key=True)
    nickname = sa.Column(sa.String(50))
