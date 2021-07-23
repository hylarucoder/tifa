import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class WarehouseStock(Model):
    __tablename__ = "warehouse_stock"
    __table_args__ = (
        sa.CheckConstraint("quantity >= 0"),
        sa.UniqueConstraint("warehouse_id", "product_variant_id"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    quantity = sa.Column(sa.Integer, nullable=False)
    product_variant_id = sa.Column(
        sa.ForeignKey(
            "product_productvariant.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    warehouse_id = sa.Column(
        sa.ForeignKey("warehouse_warehouse.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    product_variant = relationship("ProductProductvariant")
    warehouse = relationship("WarehouseWarehouse")


class WarehouseWarehouseShippingZone(Model):
    __tablename__ = "warehouse_warehouse_shipping_zones"
    __table_args__ = (sa.UniqueConstraint("warehouse_id", "shippingzone_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    warehouse_id = sa.Column(
        sa.ForeignKey("warehouse_warehouse.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    shippingzone_id = sa.Column(
        sa.ForeignKey(
            "shipping_shippingzone.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )

    shippingzone = relationship("ShippingShippingzone")
    warehouse = relationship("WarehouseWarehouse")


class WarehouseAllocation(Model):
    __tablename__ = "warehouse_allocation"
    __table_args__ = (
        sa.CheckConstraint("quantity_allocated >= 0"),
        sa.UniqueConstraint("order_line_id", "stock_id"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    quantity_allocated = sa.Column(sa.Integer, nullable=False)
    order_line_id = sa.Column(
        sa.ForeignKey("order_orderline.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    stock_id = sa.Column(
        sa.ForeignKey("warehouse_stock.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    order_line = relationship("OrderOrderline")
    stock = relationship("WarehouseStock")


class WarehouseWarehouse(Model):
    __tablename__ = "warehouse_warehouse"

    id = sa.Column(UUID, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False)
    email = sa.Column(sa.String(254), nullable=False)
    address_id = sa.Column(
        sa.ForeignKey("account_address.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)

    address = relationship("AccountAddres")
