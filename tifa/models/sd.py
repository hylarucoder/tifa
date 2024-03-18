from __future__ import annotations

import datetime

import sqlalchemy as sa
from tifa.db import Model
from sqlalchemy.orm import Mapped, mapped_column


class User(Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(100), index=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        sa.DateTime, default=datetime.datetime.now
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        sa.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
