import datetime

import sqlalchemy as sa

from tifa.globals import Model


class Merchant(Model):
    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.String(255))
    name = sa.Column(sa.String(255))
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.datetime.now)


class Staff(Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), unique=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.datetime.now)
