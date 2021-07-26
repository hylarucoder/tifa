import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.channel import Channel
from tifa.models.product_collection import ProductCategory, ProductCollection
from tifa.models.product import Product
from tifa.models.utils import TimestampMixin


class DiscountSale(TimestampMixin, Model):
    __tablename__ = "discount_sale"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    type = sa.Column(sa.String(10), nullable=False)
    end_date = sa.Column(sa.DateTime)
    start_date = sa.Column(sa.DateTime, nullable=False)


class DiscountVoucher(TimestampMixin, Model):
    __tablename__ = "discount_voucher"
    __table_args__ = (
        sa.CheckConstraint("min_checkout_items_quantity >= 0"),
        sa.CheckConstraint("usage_limit >= 0"),
        sa.CheckConstraint("used >= 0"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    type = sa.Column(sa.String(20), nullable=False)
    name = sa.Column(sa.String(255))
    code = sa.Column(sa.String(12), nullable=False, unique=True)
    usage_limit = sa.Column(sa.Integer)
    used = sa.Column(sa.Integer, nullable=False)
    start_date = sa.Column(sa.DateTime, nullable=False)
    end_date = sa.Column(sa.DateTime)
    discount_value_type = sa.Column(sa.String(10), nullable=False)
    apply_once_per_order = sa.Column(sa.Boolean, nullable=False)
    countries = sa.Column(sa.String(749), nullable=False)
    min_checkout_items_quantity = sa.Column(sa.Integer)
    apply_once_per_customer = sa.Column(sa.Boolean, nullable=False)
    only_for_staff = sa.Column(sa.Boolean, nullable=False)


class DiscountVoucherTranslation(Model):
    __tablename__ = "discount_voucher_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "voucher_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(255))
    voucher_id = sa.Column(
        sa.ForeignKey("discount_voucher.id"),
        nullable=False,
    )

    voucher = relationship(DiscountVoucher)


class DiscountSaleCategory(TimestampMixin, Model):
    __tablename__ = "discount_sale_category"
    __table_args__ = (sa.UniqueConstraint("sale_id", "category_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sale_id = sa.Column(
        sa.ForeignKey("discount_sale.id"),
        nullable=False,
    )
    sale = relationship(DiscountSale)
    category_id = sa.Column(
        sa.ForeignKey("product_category.id"),
        nullable=False,
    )

    category = relationship(ProductCategory)


class DiscountSaleCollection(TimestampMixin, Model):
    __tablename__ = "discount_sale_collection"
    __table_args__ = (sa.UniqueConstraint("sale_id", "collection_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sale_id = sa.Column(
        sa.ForeignKey("discount_sale.id"),
        nullable=False,
    )
    sale = relationship(DiscountSale)
    collection_id = sa.Column(
        sa.ForeignKey("product_collection.id"),
        nullable=False,
    )

    collection = relationship(ProductCollection)


class DiscountSaleProduct(TimestampMixin, Model):
    __tablename__ = "discount_sale_product"
    __table_args__ = (sa.UniqueConstraint("sale_id", "product_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sale_id = sa.Column(
        sa.ForeignKey("discount_sale.id"),
        nullable=False,
    )
    sale = relationship(DiscountSale)
    product_id = sa.Column(
        sa.ForeignKey("product.id"),
        nullable=False,
    )

    product = relationship(Product)


class DiscountSaleChannelListing(TimestampMixin, Model):
    __tablename__ = "discount_sale_channel_listing"
    __table_args__ = (sa.UniqueConstraint("sale_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    discount_value = sa.Column(sa.Numeric(12, 3), nullable=False)
    currency = sa.Column(sa.String(3), nullable=False)
    channel_id = sa.Column(
        sa.ForeignKey("channel.id"),
        nullable=False,
        index=True,
    )
    sale_id = sa.Column(
        sa.ForeignKey("discount_sale.id"),
        nullable=False,
        index=True,
    )

    channel = relationship(Channel)
    sale = relationship(DiscountSale)


class DiscountSaleTranslation(TimestampMixin, Model):
    __tablename__ = "discount_sale_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "sale_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(255))
    sale_id = sa.Column(
        sa.ForeignKey("discount_sale.id"),
        nullable=False,
        index=True,
    )

    sale = relationship(DiscountSale)


class DiscountVoucherCategory(TimestampMixin, Model):
    __tablename__ = "discount_voucher_category"
    __table_args__ = (sa.UniqueConstraint("voucher_id", "category_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    voucher_id = sa.Column(
        sa.ForeignKey("discount_voucher.id"),
        nullable=False,
    )
    voucher = relationship(DiscountVoucher)
    category_id = sa.Column(
        sa.ForeignKey("product_category.id"),
        nullable=False,
    )

    category = relationship(ProductCategory)


class DiscountVoucherCollection(TimestampMixin, Model):
    __tablename__ = "discount_voucher_collection"
    __table_args__ = (sa.UniqueConstraint("voucher_id", "collection_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    voucher_id = sa.Column(
        sa.ForeignKey("discount_voucher.id"),
        nullable=False,
    )
    voucher = relationship(DiscountVoucher)
    collection_id = sa.Column(
        sa.ForeignKey("product_collection.id"),
        nullable=False,
    )
    collection = relationship(ProductCollection)


class DiscountVoucherProduct(TimestampMixin, Model):
    __tablename__ = "discount_voucher_product"
    __table_args__ = (sa.UniqueConstraint("voucher_id", "product_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    voucher_id = sa.Column(
        sa.ForeignKey("discount_voucher.id"),
        nullable=False,
        index=True,
    )
    voucher = relationship(DiscountVoucher)
    product_id = sa.Column(
        sa.ForeignKey("product.id"),
        nullable=False,
        index=True,
    )
    product = relationship(Product)


class DiscountVoucherChannelListing(TimestampMixin, Model):
    __tablename__ = "discount_voucher_channel_listing"
    __table_args__ = (sa.UniqueConstraint("voucher_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    discount_value = sa.Column(sa.Numeric(12, 3), nullable=False)
    currency = sa.Column(sa.String(3), nullable=False)
    min_spent_amount = sa.Column(sa.Numeric(12, 3))
    channel_id = sa.Column(
        sa.ForeignKey("channel.id"),
        nullable=False,
    )
    channel = relationship(Channel)
    voucher_id = sa.Column(
        sa.ForeignKey("discount_voucher.id"),
        nullable=False,
    )
    voucher = relationship(DiscountVoucher)


class DiscountVoucherCustomer(Model):
    __tablename__ = "discount_voucher_customer"
    __table_args__ = (sa.UniqueConstraint("voucher_id", "customer_email"),)

    id = sa.Column(sa.Integer, primary_key=True)
    customer_email = sa.Column(sa.String(254), nullable=False)
    voucher_id = sa.Column(
        sa.ForeignKey("discount_voucher.id"),
        nullable=False,
    )
    voucher = relationship(DiscountVoucher)
