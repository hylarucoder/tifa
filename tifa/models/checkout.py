import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.utils import TimestampMixin


class Checkout(TimestampMixin, Model):
    __tablename__ = "checkout"

    created = sa.Column(sa.DateTime, nullable=False)
    last_change = sa.Column(sa.DateTime, nullable=False)
    email = sa.Column(sa.String(254), nullable=False)
    token = sa.Column(UUID, primary_key=True)
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    billing_address_id = sa.Column(
        sa.ForeignKey("account_address.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    discount_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    discount_name = sa.Column(sa.String(255))
    note = sa.Column(sa.Text, nullable=False)
    shipping_address_id = sa.Column(
        sa.ForeignKey("account_address.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    shipping_method_id = sa.Column(
        sa.ForeignKey(
            "shipping_shippingmethod.id", deferrable=True, initially="DEFERRED"
        ),
        index=True,
    )
    voucher_code = sa.Column(sa.String(12))
    translated_discount_name = sa.Column(sa.String(255))
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    currency = sa.Column(sa.String(3), nullable=False)
    country = sa.Column(sa.String(2), nullable=False)
    redirect_url = sa.Column(sa.String(200))
    tracking_code = sa.Column(sa.String(255))
    channel_id = sa.Column(
        sa.ForeignKey("channel_channel.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    language_code = sa.Column(sa.String(35), nullable=False)

    billing_address = relationship(
        "AccountAddres",
        primaryjoin="CheckoutCheckout.billing_address_id == AccountAddres.id",
    )
    channel = relationship("ChannelChannel")
    shipping_address = relationship(
        "AccountAddres",
        primaryjoin="CheckoutCheckout.shipping_address_id == AccountAddres.id",
    )
    shipping_method = relationship("ShippingShippingmethod")
    user = relationship("AccountUser")


class CheckoutCheckoutGiftCard(TimestampMixin, Model):
    __tablename__ = "checkout_gift_card"
    __table_args__ = (sa.UniqueConstraint("checkout_id", "giftcard_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    checkout_id = sa.Column(
        sa.ForeignKey("checkout_checkout.token", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    giftcard_id = sa.Column(
        sa.ForeignKey("giftcard_giftcard.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    checkout = relationship("CheckoutCheckout")
    giftcard = relationship("GiftcardGiftcard")


class CheckoutLine(TimestampMixin, Model):
    __tablename__ = "checkout_line"
    __table_args__ = (sa.CheckConstraint("quantity >= 0"),)

    id = sa.Column(sa.Integer, primary_key=True)
    quantity = sa.Column(sa.Integer, nullable=False)
    checkout_id = sa.Column(
        sa.ForeignKey("checkout_checkout.token", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    variant_id = sa.Column(
        sa.ForeignKey(
            "product_productvariant.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )

    checkout = relationship("CheckoutCheckout")
    variant = relationship("ProductProductvariant")
