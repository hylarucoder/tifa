import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.order import OrderLine
from tifa.models.product import ProductVariant
from tifa.models.shipping import ShippingZone
from tifa.models.address import Address


class Warehouse(Model):
    __tablename__ = "warehouse"

    id = sa.Column(UUID, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False)
    email = sa.Column(sa.String(254), nullable=False)
    address_id = sa.Column(sa.ForeignKey("address.id"), nullable=False)
    address = relationship(Address)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)


class WarehouseStock(Model):
    __tablename__ = "warehouse_stock"
    __table_args__ = (
        sa.CheckConstraint("quantity >= 0"),
        sa.UniqueConstraint("warehouse_id", "product_variant_id"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    quantity = sa.Column(sa.Integer, nullable=False)
    product_variant_id = sa.Column(
        sa.ForeignKey("product_variant.id"),
        nullable=False,
    )
    product_variant = relationship(ProductVariant)

    warehouse_id = sa.Column(
        sa.ForeignKey("warehouse.id"),
        nullable=False,
    )
    warehouse = relationship(Warehouse)


class WarehouseShippingZone(Model):
    __tablename__ = "warehouse_shipping_zone"
    __table_args__ = (sa.UniqueConstraint("warehouse_id", "shipping_zone_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    warehouse_id = sa.Column(
        sa.ForeignKey("warehouse.id"),
        nullable=False,
    )
    shipping_zone_id = sa.Column(
        sa.ForeignKey("shipping_zone.id"),
        nullable=False,
    )

    shipping_zone = relationship(ShippingZone)
    warehouse = relationship(Warehouse)


class WarehouseAllocation(Model):
    __tablename__ = "warehouse_allocation"
    __table_args__ = (
        sa.CheckConstraint("quantity_allocated >= 0"),
        sa.UniqueConstraint("order_line_id", "stock_id"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    quantity_allocated = sa.Column(sa.Integer, nullable=False)
    order_line_id = sa.Column(
        sa.ForeignKey("order_line.id"),
        nullable=False,
    )
    order_line = relationship(OrderLine)
    stock_id = sa.Column(
        sa.ForeignKey("warehouse_stock.id"),
        nullable=False,
    )
    stock = relationship(WarehouseStock)
