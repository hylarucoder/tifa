import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.product_collection import ProductCollection
from tifa.models.utils import TimestampMixin


class Channel(TimestampMixin, Model):
    __tablename__ = "channel"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    is_active = sa.Column(sa.Boolean, nullable=False)
    currency_code = sa.Column(sa.String(3), nullable=False)


class ProductChannelListing(Model):
    __tablename__ = "product_channel_listing"
    __table_args__ = (sa.UniqueConstraint("product_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    publication_date = sa.Column(sa.Date, index=True)
    is_published = sa.Column(sa.Boolean, nullable=False)
    channel_id = sa.Column(sa.ForeignKey("channel.id"), nullable=False)
    channel = relationship(Channel)
    product_id = sa.Column(sa.ForeignKey("product.id"), nullable=False)
    product = relationship("Product")
    discounted_price_amount = sa.Column(sa.Numeric(12, 3))
    currency = sa.Column(sa.String(3), nullable=False)
    visible_in_listings = sa.Column(sa.Boolean, nullable=False)
    available_for_purchase = sa.Column(sa.Date)


class ProductVariantChannelListing(Model):
    __tablename__ = "product_variant_channel_listing"
    __table_args__ = (sa.UniqueConstraint("variant_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    currency = sa.Column(sa.String(3), nullable=False)
    price_amount = sa.Column(sa.Numeric(12, 3))
    channel_id = sa.Column(
        sa.ForeignKey("channel.id"),
        nullable=False,
    )
    channel = relationship(Channel)
    variant_id = sa.Column(
        sa.ForeignKey("product_variant.id"),
        nullable=False,
    )
    variant = relationship("ProductVariant")
    cost_price_amount = sa.Column(sa.Numeric(12, 3))


class ProductCollectionChannelListing(Model):
    __tablename__ = "product_collection_channel_listing"
    __table_args__ = (sa.UniqueConstraint("collection_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    publication_date = sa.Column(sa.Date)
    is_published = sa.Column(sa.Boolean, nullable=False)
    channel_id = sa.Column(sa.ForeignKey("channel.id"), nullable=False)
    channel = relationship(Channel)
    collection_id = sa.Column(sa.ForeignKey("product_collection.id"), nullable=False)
    collection = relationship(ProductCollection)
