import sqlalchemy as sa

from tifa.globals import Model


class Post(Model):
    __tablename__ = "post"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50))
