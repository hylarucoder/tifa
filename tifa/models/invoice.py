import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class InvoiceInvoice(Model):
    __tablename__ = "invoice"

    id = sa.Column(sa.Integer, primary_key=True)
    metadata_private = sa.Column(JSONB, index=True)
    metadata_public = sa.Column(JSONB, index=True)
    status = sa.Column(sa.String(50), nullable=False)
    created_at = sa.Column(sa.DateTime(True), nullable=False)
    updated_at = sa.Column(sa.DateTime(True), nullable=False)
    number = sa.Column(sa.String(255))
    created = sa.Column(sa.DateTime(True))
    external_url = sa.Column(sa.String(2048))
    invoice_file = sa.Column(sa.String(100), nullable=False)
    order_id = sa.Column(
        sa.ForeignKey("order_order.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    message = sa.Column(sa.String(255))

    order = relationship("OrderOrder")


class InvoiceInvoiceEvent(Model):
    __tablename__ = "invoice_event"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime(True), nullable=False)
    type = sa.Column(sa.String(255), nullable=False)
    parameters = sa.Column(JSONB, nullable=False)
    invoice_id = sa.Column(
        sa.ForeignKey("invoice_invoice.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    order_id = sa.Column(
        sa.ForeignKey("order_order.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    app_id = sa.Column(
        sa.ForeignKey("app_app.id", deferrable=True, initially="DEFERRED"), index=True
    )

    app = relationship("AppApp")
    invoice = relationship("InvoiceInvoice")
    order = relationship("OrderOrder")
    user = relationship("AccountUser")
