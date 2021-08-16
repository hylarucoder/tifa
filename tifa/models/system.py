import datetime

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model


class Staff(Model):
    __tablename__ = "staff"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), unique=True)
    password_hash = sa.Column(sa.String(255))
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.datetime.now)


class Permission(Model):
    __tablename__ = "permission"
    id = sa.Column(sa.Integer, primary_key=True)


class StaffNotificationRecipient(Model):
    __tablename__ = "staff_notification_recipient"

    id = sa.Column(sa.Integer, primary_key=True)
    is_active = sa.Column(sa.Boolean, nullable=False)
    staff_email = sa.Column(sa.String(254), unique=True)
    staff_id = sa.Column(sa.ForeignKey("staff.id"), unique=True)
    staff = relationship(Staff, uselist=False)
