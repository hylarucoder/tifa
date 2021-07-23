import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.app import App


class Webhook(Model):
    __tablename__ = "webhook"

    id = sa.Column(sa.Integer, primary_key=True)
    target_url = sa.Column(sa.String(255), nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False)
    secret_key = sa.Column(sa.String(255))
    app_id = sa.Column(
        sa.ForeignKey("app.id"),
        nullable=False,
    )
    app = relationship(App)
    name = sa.Column(sa.String(255))


class WebhookEvent(Model):
    __tablename__ = "webhook_event"

    id = sa.Column(sa.Integer, primary_key=True)
    event_type = sa.Column(sa.String(128), nullable=False, index=True)
    webhook_id = sa.Column(
        sa.ForeignKey("webhook.id"),
        nullable=False,
    )

    webhook = relationship(Webhook)
