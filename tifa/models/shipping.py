import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.channel import Channel
from tifa.models.product import Product


class ShippingZone(Model):
    __tablename__ = "shipping_zone"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    countries = sa.Column(sa.String(749), nullable=False)
    default = sa.Column(sa.Boolean, nullable=False)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    description = sa.Column(sa.Text, nullable=False)


class ShippingMethod(Model):
    __tablename__ = "shipping_method"
    __table_args__ = (
        sa.CheckConstraint("maximum_delivery_days >= 0"),
        sa.CheckConstraint("minimum_delivery_days >= 0"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    maximum_order_weight = sa.Column(sa.Float(53))
    minimum_order_weight = sa.Column(sa.Float(53))
    type = sa.Column(sa.String(30), nullable=False)
    shipping_zone_id = sa.Column(
        sa.ForeignKey("shipping_zone.id"),
        nullable=False,
    )
    shipping_zone = relationship(ShippingZone)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    maximum_delivery_days = sa.Column(sa.Integer)
    minimum_delivery_days = sa.Column(sa.Integer)
    description = sa.Column(JSONB)


class ShippingZoneChannel(Model):
    __tablename__ = "shipping_zone_channel"
    __table_args__ = (sa.UniqueConstraint("shipping_zone_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    shipping_zone_id = sa.Column(
        sa.ForeignKey(
            "shipping_zone.id"
        ),
        nullable=False,
    )
    shipping_zone = relationship(ShippingZone)
    channel_id = sa.Column(sa.ForeignKey("channel.id"), nullable=False, )
    channel = relationship(Channel)


class ShippingMethodExcludedProduct(Model):
    __tablename__ = "shipping_method_excluded_product"
    __table_args__ = (sa.UniqueConstraint("shipping_method_id", "product_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    shipping_method_id = sa.Column(sa.ForeignKey("shipping_method.id"), nullable=False)
    shipping_method = relationship(ShippingMethod)
    product_id = sa.Column(sa.ForeignKey("product.id"), nullable=False, )
    product = relationship(Product)


class ShippingMethodChannelListing(Model):
    __tablename__ = "shipping_method_channel_listing"
    __table_args__ = (sa.UniqueConstraint("shipping_method_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    minimum_order_price_amount = sa.Column(sa.Numeric(12, 3))
    currency = sa.Column(sa.String(3), nullable=False)
    maximum_order_price_amount = sa.Column(sa.Numeric(12, 3))
    price_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    channel_id = sa.Column(sa.ForeignKey("channel.id"), nullable=False, )
    channel = relationship(Channel)
    shipping_method_id = sa.Column(sa.ForeignKey("shipping_method.id"), nullable=False, )
    shipping_method = relationship(ShippingMethod)


class ShippingMethodPostalCodeRule(Model):
    __tablename__ = "shipping_method_postal_code_rule"
    __table_args__ = (sa.UniqueConstraint("shipping_method_id", "start", "end"),)

    id = sa.Column(sa.Integer, primary_key=True)
    start = sa.Column(sa.String(32), nullable=False)
    end = sa.Column(sa.String(32))
    shipping_method_id = sa.Column(sa.ForeignKey("shipping_method.id"), nullable=False, )
    shipping_method = relationship(ShippingMethod)
    inclusion_type = sa.Column(sa.String(32), nullable=False)


class ShippingMethodTranslation(Model):
    __tablename__ = "shipping_method_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "shipping_method_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(255))
    shipping_method_id = sa.Column(sa.ForeignKey("shipping_method.id"), nullable=False, )
    shipping_method = relationship(ShippingMethod)
    description = sa.Column(JSONB)
