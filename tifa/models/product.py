import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, TSVECTOR, UUID
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.product_collection import ProductCategory, ProductCollection
from tifa.models.utils import TimestampMixin


class ProductType(TimestampMixin, Model):
    __tablename__ = "product_type"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False)
    has_variants = sa.Column(sa.Boolean, nullable=False)
    is_shipping_required = sa.Column(sa.Boolean, nullable=False)
    weight = sa.Column(sa.Float(53), nullable=False)
    is_digital = sa.Column(sa.Boolean, nullable=False)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)


class Product(TimestampMixin, Model):
    __tablename__ = "product"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False)
    description = sa.Column(JSONB)
    description_plaintext = sa.Column(sa.Text, nullable=False)
    product_type_id = sa.Column(
        sa.ForeignKey("product_type.id"),
        nullable=False,
    )
    product_type = relationship(ProductType)
    category_id = sa.Column(
        sa.ForeignKey("product_category.id"),
    )
    category = relationship(ProductCategory)
    seo_description = sa.Column(sa.String(300))
    seo_title = sa.Column(sa.String(70))
    charge_taxes = sa.Column(sa.Boolean, nullable=False)
    weight = sa.Column(sa.Float(53))
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    default_variant_id = sa.Column(
        sa.ForeignKey(
            "product_variant.id", use_alter=True, name="fk_product_default_variant_id"
        ),
        unique=True,
    )
    default_variant = relationship(
        "ProductVariant",
        uselist=False,
        primaryjoin="Product.default_variant_id == ProductVariant.id",
    )
    search_vector = sa.Column(TSVECTOR, index=True)
    rating = sa.Column(sa.Float(53))


class ProductTranslation(TimestampMixin, Model):
    __tablename__ = "product_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "product_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    seo_title = sa.Column(sa.String(70))
    seo_description = sa.Column(sa.String(300))
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(250))
    description = sa.Column(JSONB)
    product_id = sa.Column(
        sa.ForeignKey("product.id"),
        nullable=False,
    )


class ProductVariant(TimestampMixin, Model):
    __tablename__ = "product_variant"

    id = sa.Column(sa.Integer, primary_key=True)
    sku = sa.Column(sa.String(255), nullable=False, unique=True)
    name = sa.Column(sa.String(255), nullable=False)
    product_id = sa.Column(sa.ForeignKey("product.id"), nullable=False)
    product = relationship("Product", foreign_keys=[product_id])
    track_inventory = sa.Column(sa.Boolean, nullable=False)
    weight = sa.Column(sa.Float(53))
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    sort_order = sa.Column(sa.Integer, index=True)


class ProductVariantTranslation(TimestampMixin, Model):
    __tablename__ = "product_variant_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "product_variant_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(255), nullable=False)
    product_variant_id = sa.Column(
        sa.ForeignKey("product_variant.id"),
        nullable=False,
    )

    product_variant = relationship(ProductVariant)


class CollectionProduct(TimestampMixin, Model):
    __tablename__ = "collection_product"
    __table_args__ = (sa.UniqueConstraint("collection_id", "product_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    collection_id = sa.Column(
        sa.ForeignKey("product_collection.id"),
        nullable=False,
    )
    product_id = sa.Column(
        sa.ForeignKey("product.id"),
        nullable=False,
    )
    sort_order = sa.Column(sa.Integer, index=True)
    collection = relationship(ProductCollection)
    product = relationship(Product)


class ProductDigitalContent(TimestampMixin, Model):
    __tablename__ = "product_digital_content"

    id = sa.Column(sa.Integer, primary_key=True)
    use_default_settings = sa.Column(sa.Boolean, nullable=False)
    automatic_fulfillment = sa.Column(sa.Boolean, nullable=False)
    content_type = sa.Column(sa.String(128), nullable=False)
    content_file = sa.Column(sa.String(100), nullable=False)
    max_downloads = sa.Column(sa.Integer)
    url_valid_days = sa.Column(sa.Integer)
    product_variant_id = sa.Column(
        sa.ForeignKey("product_variant.id"),
        nullable=False,
        unique=True,
    )
    product_variant = relationship(ProductVariant, uselist=False)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)


class ProductDigitalContentUrl(Model):
    __tablename__ = "product_digital_content_url"

    id = sa.Column(sa.Integer, primary_key=True)
    token = sa.Column(UUID, nullable=False, unique=True)
    created = sa.Column(sa.DateTime, nullable=False)
    download_num = sa.Column(sa.Integer, nullable=False)
    content_id = sa.Column(
        sa.ForeignKey("product_digital_content.id"),
        nullable=False,
        index=True,
    )
    content = relationship(ProductDigitalContent)
    line_id = sa.Column(
        sa.ForeignKey("order_line.id"),
        unique=True,
    )
    line = relationship("OrderLine", uselist=False)
