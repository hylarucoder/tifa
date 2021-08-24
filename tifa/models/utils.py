import datetime
from sqlalchemy.dialects.postgresql import JSONB
import sqlalchemy as sa


class TimestampMixin:
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.datetime.now)


class MetadataMixin:
    metadata_private = sa.Column(JSONB, index=True)
    metadata_public = sa.Column(JSONB, index=True)


class SortableMixin:
    sort_order = sa.Column(sa.Integer, index=True)
