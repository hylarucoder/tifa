from tifa.globals import db
from tifa.models.base import ModelMixin
import sqlalchemy as sa


class Post(ModelMixin, db.Model):
    __tablename__ = "post"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50))
