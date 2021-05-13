import sqlalchemy as sa


class BaseModel:
    created_at = sa.Column(
        sa.DateTime,
    )
    updated_at = sa.Column(
        sa.DateTime,
    )
