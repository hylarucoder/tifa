import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.utils import TimestampMixin


class Channel(TimestampMixin, Model):
    __tablename__ = "channel"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    is_active = sa.Column(sa.Boolean, nullable=False)
    currency_code = sa.Column(sa.String(3), nullable=False)


class ProductProductChannelListing(Model):
    __tablename__ = "product_productchannellisting"
    __table_args__ = (sa.UniqueConstraint("product_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    publication_date = sa.Column(sa.Date, index=True)
    is_published = sa.Column(sa.Boolean, nullable=False)
    channel_id = sa.Column(
        sa.ForeignKey("channel_channel.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    product_id = sa.Column(
        sa.ForeignKey("product_product.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    discounted_price_amount = sa.Column(sa.Numeric(12, 3))
    currency = sa.Column(sa.String(3), nullable=False)
    visible_in_listings = sa.Column(sa.Boolean, nullable=False)
    available_for_purchase = sa.Column(sa.Date)

    channel = relationship("ChannelChannel")
    product = relationship("ProductProduct")


class ProductVariantChannelListing(Model):
    __tablename__ = "product_productvariantchannellisting"
    __table_args__ = (sa.UniqueConstraint("variant_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    currency = sa.Column(sa.String(3), nullable=False)
    price_amount = sa.Column(sa.Numeric(12, 3))
    channel_id = sa.Column(
        sa.ForeignKey("channel_channel.id", deferrable=True, initially="DEFERRED"),
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
    cost_price_amount = sa.Column(sa.Numeric(12, 3))

    channel = relationship("ChannelChannel")
    variant = relationship("ProductProductvariant")
