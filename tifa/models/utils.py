import datetime

import sqlalchemy as sa


class TimestampMixin:
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.datetime.now)
