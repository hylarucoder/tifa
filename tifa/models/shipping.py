import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class ShippingShippingmethod(Model):
    __tablename__ = "shipping_shippingmethod"
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
        sa.ForeignKey(
            "shipping_shippingzone.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    maximum_delivery_days = sa.Column(sa.Integer)
    minimum_delivery_days = sa.Column(sa.Integer)
    description = sa.Column(JSONB)

    shipping_zone = relationship("ShippingShippingzone")


class ShippingShippingzoneChannel(Model):
    __tablename__ = "shipping_shippingzone_channels"
    __table_args__ = (sa.UniqueConstraint("shippingzone_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    shippingzone_id = sa.Column(
        sa.ForeignKey(
            "shipping_shippingzone.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    channel_id = sa.Column(
        sa.ForeignKey("channel_channel.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    channel = relationship("ChannelChannel")
    shippingzone = relationship("ShippingShippingzone")


class ShippingShippingmethodExcludedProduct(Model):
    __tablename__ = "shipping_shippingmethod_excluded_products"
    __table_args__ = (sa.UniqueConstraint("shippingmethod_id", "product_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    shippingmethod_id = sa.Column(
        sa.ForeignKey(
            "shipping_shippingmethod.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    product_id = sa.Column(
        sa.ForeignKey("product_product.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    product = relationship("ProductProduct")
    shippingmethod = relationship("ShippingShippingmethod")


class ShippingShippingmethodchannellisting(Model):
    __tablename__ = "shipping_shippingmethodchannellisting"
    __table_args__ = (sa.UniqueConstraint("shipping_method_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    minimum_order_price_amount = sa.Column(sa.Numeric(12, 3))
    currency = sa.Column(sa.String(3), nullable=False)
    maximum_order_price_amount = sa.Column(sa.Numeric(12, 3))
    price_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    channel_id = sa.Column(
        sa.ForeignKey("channel_channel.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    shipping_method_id = sa.Column(
        sa.ForeignKey(
            "shipping_shippingmethod.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )

    channel = relationship("ChannelChannel")
    shipping_method = relationship("ShippingShippingmethod")


class ShippingShippingmethodpostalcoderule(Model):
    __tablename__ = "shipping_shippingmethodpostalcoderule"
    __table_args__ = (sa.UniqueConstraint("shipping_method_id", "start", "end"),)

    id = sa.Column(sa.Integer, primary_key=True)
    start = sa.Column(sa.String(32), nullable=False)
    end = sa.Column(sa.String(32))
    shipping_method_id = sa.Column(
        sa.ForeignKey(
            "shipping_shippingmethod.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    inclusion_type = sa.Column(sa.String(32), nullable=False)

    shipping_method = relationship("ShippingShippingmethod")


class ShippingShippingmethodtranslation(Model):
    __tablename__ = "shipping_shippingmethodtranslation"
    __table_args__ = (sa.UniqueConstraint("language_code", "shipping_method_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(255))
    shipping_method_id = sa.Column(
        sa.ForeignKey(
            "shipping_shippingmethod.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    description = sa.Column(JSONB)

    shipping_method = relationship("ShippingShippingmethod")


class ShippingShippingzone(Model):
    __tablename__ = "shipping_shippingzone"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    countries = sa.Column(sa.String(749), nullable=False)
    default = sa.Column(sa.Boolean, nullable=False)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    description = sa.Column(sa.Text, nullable=False)
