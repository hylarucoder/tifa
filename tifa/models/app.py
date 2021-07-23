import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class App(Model):
    __tablename__ = "app"

    id = sa.Column(sa.Integer, primary_key=True)
    metadata_private = sa.Column(JSONB, index=True)
    metadata_public = sa.Column(JSONB, index=True)
    name = sa.Column(sa.String(60), nullable=False)
    created = sa.Column(sa.DateTime(True), nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False)
    about_app = sa.Column(sa.Text)
    app_url = sa.Column(sa.String(200))
    configuration_url = sa.Column(sa.String(200))
    data_privacy = sa.Column(sa.Text)
    data_privacy_url = sa.Column(sa.String(200))
    homepage_url = sa.Column(sa.String(200))
    identifier = sa.Column(sa.String(256))
    support_url = sa.Column(sa.String(200))
    type = sa.Column(sa.String(60), nullable=False)
    version = sa.Column(sa.String(60))


class AppInstallation(Model):
    __tablename__ = "app_installation"

    id = sa.Column(sa.Integer, primary_key=True)
    status = sa.Column(sa.String(50), nullable=False)
    message = sa.Column(sa.String(255))
    created_at = sa.Column(sa.DateTime(True), nullable=False)
    updated_at = sa.Column(sa.DateTime(True), nullable=False)
    app_name = sa.Column(sa.String(60), nullable=False)
    manifest_url = sa.Column(sa.String(200), nullable=False)


class AppToken(Model):
    __tablename__ = "app_token"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(128), nullable=False)
    auth_token = sa.Column(sa.String(30), nullable=False, unique=True)
    app_id = sa.Column(
        sa.ForeignKey("app_app.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    app = relationship("AppApp")


class AppPermission(Model):
    __tablename__ = "app_app_permissions"
    __table_args__ = (sa.UniqueConstraint("app_id", "permission_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    app_id = sa.Column(
        sa.ForeignKey("app_app.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    permission_id = sa.Column(
        sa.ForeignKey("auth_permission.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    app = relationship("AppApp")
    permission = relationship("AuthPermission")


class AppInstallationPermission(Model):
    __tablename__ = "app_installation_permissions"
    __table_args__ = (sa.UniqueConstraint("appinstallation_id", "permission_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    app_installation_id = sa.Column(
        sa.ForeignKey("app_installation.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    permission_id = sa.Column(
        sa.ForeignKey("auth_permission.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    app_installation = relationship("AppAppinstallation")
    permission = relationship("AuthPermission")
