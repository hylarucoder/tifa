import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.app import App
from tifa.models.order import Order
from tifa.models.user import User


class Invoice(Model):
    __tablename__ = "invoice"

    id = sa.Column(sa.Integer, primary_key=True)
    order_id = sa.Column(
        sa.ForeignKey("order.id"),
    )
    order = relationship(Order)
    metadata_private = sa.Column(JSONB, index=True)
    metadata_public = sa.Column(JSONB, index=True)
    status = sa.Column(sa.String(50), nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False)
    updated_at = sa.Column(sa.DateTime, nullable=False)
    number = sa.Column(sa.String(255))
    created = sa.Column(sa.DateTime)
    external_url = sa.Column(sa.String(2048))
    invoice_file = sa.Column(sa.String(100), nullable=False)
    message = sa.Column(sa.String(255))


class InvoiceEvent(Model):
    __tablename__ = "invoice_event"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime, nullable=False)
    type = sa.Column(sa.String(255), nullable=False)
    parameters = sa.Column(JSONB, nullable=False)
    invoice_id = sa.Column(
        sa.ForeignKey("invoice.id"),
    )
    invoice = relationship(Invoice)
    order_id = sa.Column(sa.ForeignKey("order.id"))
    order = relationship(Order)
    user_id = sa.Column(sa.ForeignKey("user.id"))
    user = relationship(User)
    app_id = sa.Column(sa.ForeignKey("app.id"))
    app = relationship(App)
