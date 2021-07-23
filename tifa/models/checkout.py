import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.channel import Channel
from tifa.models.gift_card import GiftCard
from tifa.models.product import ProductVariant
from tifa.models.shipping import ShippingMethod
from tifa.models.user import User
from tifa.models.address import Address
from tifa.models.utils import TimestampMixin


class Checkout(TimestampMixin, Model):
    __tablename__ = "checkout"

    id = sa.Column(UUID, primary_key=True)
    created = sa.Column(sa.DateTime, nullable=False)
    last_change = sa.Column(sa.DateTime, nullable=False)
    email = sa.Column(sa.String(254), nullable=False)
    user_id = sa.Column(sa.ForeignKey("user.id"))
    user = relationship(User)
    billing_address_id = sa.Column(sa.ForeignKey("address.id"))
    billing_address = relationship(Address, primaryjoin="Checkout.billing_address_id == Address.id")
    channel_id = sa.Column(sa.ForeignKey("channel.id"), nullable=False, )
    channel = relationship(Channel)
    shipping_address = relationship(Address, primaryjoin="Checkout.shipping_address_id == Address.id")
    shipping_method_id = sa.Column(sa.ForeignKey("shipping_method.id"))
    shipping_method = relationship(ShippingMethod)
    discount_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    discount_name = sa.Column(sa.String(255))
    note = sa.Column(sa.Text, nullable=False)
    shipping_address_id = sa.Column(sa.ForeignKey("address.id"))
    voucher_code = sa.Column(sa.String(12))
    translated_discount_name = sa.Column(sa.String(255))
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    currency = sa.Column(sa.String(3), nullable=False)
    country = sa.Column(sa.String(2), nullable=False)
    redirect_url = sa.Column(sa.String(200))
    tracking_code = sa.Column(sa.String(255))
    language_code = sa.Column(sa.String(35), nullable=False)


class CheckoutGiftCard(TimestampMixin, Model):
    __tablename__ = "checkout_gift_card"
    __table_args__ = (sa.UniqueConstraint("checkout_id", "gift_card_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    checkout_id = sa.Column(sa.ForeignKey("checkout.id"), nullable=False)
    checkout = relationship(Checkout)
    gift_card_id = sa.Column(sa.ForeignKey("gift_card.id"), nullable=False)
    gift_card = relationship(GiftCard)


class CheckoutLine(TimestampMixin, Model):
    __tablename__ = "checkout_line"
    __table_args__ = (sa.CheckConstraint("quantity >= 0"),)

    id = sa.Column(sa.Integer, primary_key=True)
    quantity = sa.Column(sa.Integer, nullable=False)
    checkout_id = sa.Column(sa.ForeignKey("checkout.id"), nullable=False)
    checkout = relationship(Checkout)
    variant_id = sa.Column(sa.ForeignKey("product_variant.id"), nullable=False)
    variant = relationship(ProductVariant)
