import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.system import Permission
from tifa.models.utils import TimestampMixin, MetadataMixin


class App(MetadataMixin, Model):
    __tablename__ = "app"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(60), nullable=False)
    created = sa.Column(sa.DateTime, nullable=False)
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


class AppInstallation(TimestampMixin, Model):
    __tablename__ = "app_installation"

    id = sa.Column(sa.Integer, primary_key=True)
    status = sa.Column(sa.String(50), nullable=False)
    message = sa.Column(sa.String(255))
    app_name = sa.Column(sa.String(60), nullable=False)
    manifest_url = sa.Column(sa.String(200), nullable=False)


class AppToken(Model):
    __tablename__ = "app_token"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(128), nullable=False)
    auth_token = sa.Column(sa.String(30), nullable=False, unique=True)
    app_id = sa.Column(sa.ForeignKey("app.id"), nullable=False)
    app = relationship(App)


class AppPermission(Model):
    __tablename__ = "app_permission"
    __table_args__ = (sa.UniqueConstraint("app_id", "permission_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    app_id = sa.Column(sa.ForeignKey("app.id"), nullable=False)

    app = relationship(App)
    permission_id = sa.Column(sa.ForeignKey("permission.id"), nullable=False)
    permission = relationship(Permission)


class AppInstallationPermission(Model):
    __tablename__ = "app_installation_permissions"
    __table_args__ = (sa.UniqueConstraint("app_installation_id", "permission_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    app_installation_id = sa.Column(
        sa.ForeignKey("app_installation.id"),
        nullable=False,
        index=True,
    )
    app_installation = relationship(AppInstallation)
    permission_id = sa.Column(
        sa.ForeignKey("permission.id"),
        nullable=False,
    )
    permission = relationship(Permission)
