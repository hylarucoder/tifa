import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model


class WebhookWebhook(Model):
    __tablename__ = "webhook_webhook"

    id = sa.Column(sa.Integer, primary_key=True)
    target_url = sa.Column(sa.String(255), nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False)
    secret_key = sa.Column(sa.String(255))
    app_id = sa.Column(
        sa.ForeignKey("app_app.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    name = sa.Column(sa.String(255))

    app = relationship("AppApp")


class WebhookWebhookevent(Model):
    __tablename__ = "webhook_webhookevent"

    id = sa.Column(sa.Integer, primary_key=True)
    event_type = sa.Column(sa.String(128), nullable=False, index=True)
    webhook_id = sa.Column(
        sa.ForeignKey("webhook_webhook.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    webhook = relationship("WebhookWebhook")
