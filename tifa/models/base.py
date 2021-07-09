from __future__ import annotations

import sqlalchemy as sa


class ModelMixin:
    created_at = sa.Column(
        sa.DateTime,
    )
    updated_at = sa.Column(
        sa.DateTime,
    )


class ContentTypeMixin:
    object_type = sa.Column(sa.String(255))
    object_id = sa.Column(sa.BigInteger)
