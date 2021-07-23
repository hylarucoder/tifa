import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class Order(Model):
    __tablename__ = "order"

    id = sa.Column(sa.Integer, primary_key=True)
    created = sa.Column(sa.DateTime(True), nullable=False)
    tracking_client_id = sa.Column(sa.String(36), nullable=False)
    user_email = sa.Column(sa.String(254), nullable=False, index=True)
    token = sa.Column(sa.String(36), nullable=False, unique=True)
    billing_address_id = sa.Column(
        sa.ForeignKey("account_address.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    shipping_address_id = sa.Column(
        sa.ForeignKey("account_address.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    total_net_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    voucher_id = sa.Column(
        sa.ForeignKey("discount_voucher.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    language_code = sa.Column(sa.String(35), nullable=False)
    shipping_price_gross_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    total_gross_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    shipping_price_net_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    status = sa.Column(sa.String(32), nullable=False)
    shipping_method_name = sa.Column(sa.String(255))
    shipping_method_id = sa.Column(
        sa.ForeignKey(
            "shipping_shippingmethod.id", deferrable=True, initially="DEFERRED"
        ),
        index=True,
    )
    display_gross_prices = sa.Column(sa.Boolean, nullable=False)
    customer_note = sa.Column(sa.Text, nullable=False)
    weight = sa.Column(sa.Float(53), nullable=False)
    checkout_token = sa.Column(sa.String(36), nullable=False)
    currency = sa.Column(sa.String(3), nullable=False)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    channel_id = sa.Column(
        sa.ForeignKey("channel_channel.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    redirect_url = sa.Column(sa.String(200))
    shipping_tax_rate = sa.Column(sa.Numeric(5, 4), nullable=False)
    undiscounted_total_gross_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    undiscounted_total_net_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    total_paid_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    origin = sa.Column(sa.String(32), nullable=False)
    original_id = sa.Column(
        sa.ForeignKey("order_order.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )

    billing_address = relationship(
        "AccountAddres", primaryjoin="OrderOrder.billing_address_id == AccountAddres.id"
    )
    channel = relationship("ChannelChannel")
    original = relationship("OrderOrder", remote_side=[id])
    shipping_address = relationship(
        "AccountAddres",
        primaryjoin="OrderOrder.shipping_address_id == AccountAddres.id",
    )
    shipping_method = relationship("ShippingShippingmethod")
    user = relationship("AccountUser")
    voucher = relationship("DiscountVoucher")


class OrderFulfillment(Model):
    __tablename__ = "order_fulfillment"
    __table_args__ = (sa.CheckConstraint("fulfillment_order >= 0"),)

    id = sa.Column(sa.Integer, primary_key=True)
    tracking_number = sa.Column(sa.String(255), nullable=False)
    created = sa.Column(sa.DateTime(True), nullable=False)
    order_id = sa.Column(
        sa.ForeignKey("order_order.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    fulfillment_order = sa.Column(sa.Integer, nullable=False)
    status = sa.Column(sa.String(32), nullable=False)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    shipping_refund_amount = sa.Column(sa.Numeric(12, 3))
    total_refund_amount = sa.Column(sa.Numeric(12, 3))

    order = relationship("OrderOrder")


class OrderGiftCard(Model):
    __tablename__ = "order_order_gift_cards"
    __table_args__ = (sa.UniqueConstraint("order_id", "giftcard_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    order_id = sa.Column(
        sa.ForeignKey("order_order.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    giftcard_id = sa.Column(
        sa.ForeignKey("giftcard_giftcard.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    giftcard = relationship("GiftcardGiftcard")
    order = relationship("OrderOrder")


class OrderEvent(Model):
    __tablename__ = "order_orderevent"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime(True), nullable=False)
    type = sa.Column(sa.String(255), nullable=False)
    order_id = sa.Column(
        sa.ForeignKey("order_order.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    parameters = sa.Column(JSONB, nullable=False)
    app_id = sa.Column(
        sa.ForeignKey("app_app.id", deferrable=True, initially="DEFERRED"), index=True
    )

    app = relationship("AppApp")
    order = relationship("OrderOrder")
    user = relationship("AccountUser")


class OrderLine(Model):
    __tablename__ = "order_orderline"

    id = sa.Column(sa.Integer, primary_key=True)
    product_name = sa.Column(sa.String(386), nullable=False)
    product_sku = sa.Column(sa.String(255), nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    unit_price_net_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    unit_price_gross_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    is_shipping_required = sa.Column(sa.Boolean, nullable=False)
    order_id = sa.Column(
        sa.ForeignKey("order_order.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    quantity_fulfilled = sa.Column(sa.Integer, nullable=False)
    variant_id = sa.Column(
        sa.ForeignKey(
            "product_productvariant.id", deferrable=True, initially="DEFERRED"
        ),
        index=True,
    )
    tax_rate = sa.Column(sa.Numeric(5, 4), nullable=False)
    translated_product_name = sa.Column(sa.String(386), nullable=False)
    currency = sa.Column(sa.String(3), nullable=False)
    translated_variant_name = sa.Column(sa.String(255), nullable=False)
    variant_name = sa.Column(sa.String(255), nullable=False)
    total_price_gross_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    total_price_net_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    unit_discount_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    unit_discount_value = sa.Column(sa.Numeric(12, 3), nullable=False)
    unit_discount_reason = sa.Column(sa.Text)
    unit_discount_type = sa.Column(sa.String(10), nullable=False)
    undiscounted_total_price_gross_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    undiscounted_total_price_net_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    undiscounted_unit_price_gross_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    undiscounted_unit_price_net_amount = sa.Column(sa.Numeric(12, 3), nullable=False)

    order = relationship("OrderOrder")
    variant = relationship("ProductProductvariant")


class OrderFulfillmentline(Model):
    __tablename__ = "order_fulfillmentline"
    __table_args__ = (sa.CheckConstraint("quantity >= 0"),)

    id = sa.Column(sa.Integer, primary_key=True)
    order_line_id = sa.Column(
        sa.ForeignKey("order_orderline.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    quantity = sa.Column(sa.Integer, nullable=False)
    fulfillment_id = sa.Column(
        sa.ForeignKey("order_fulfillment.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    stock_id = sa.Column(
        sa.ForeignKey("warehouse_stock.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )

    fulfillment = relationship("OrderFulfillment")
    order_line = relationship("OrderOrderline")
    stock = relationship("WarehouseStock")


class DiscountOrderDiscount(Model):
    __tablename__ = "discount_order_discount"
    __table_args__ = (
        sa.Index("discount_or_name_d16858_gin", "name", "translated_name"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    type = sa.Column(sa.String(10), nullable=False)
    value_type = sa.Column(sa.String(10), nullable=False)
    value = sa.Column(sa.Numeric(12, 3), nullable=False)
    amount_value = sa.Column(sa.Numeric(12, 3), nullable=False)
    currency = sa.Column(sa.String(3), nullable=False)
    name = sa.Column(sa.String(255))
    translated_name = sa.Column(sa.String(255))
    reason = sa.Column(sa.Text)
    order_id = sa.Column(
        sa.ForeignKey("order_order.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )

    order = relationship("OrderOrder")
