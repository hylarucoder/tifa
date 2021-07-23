import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, TSVECTOR, UUID
from sqlalchemy.orm import relationship

from tifa.globals import Model


class ProductType(Model):
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


class Product(Model):
    __tablename__ = "product"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False)
    description = sa.Column(JSONB)
    updated_at = sa.Column(sa.DateTime(True))
    product_type_id = sa.Column(
        sa.ForeignKey("product_producttype.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    category_id = sa.Column(
        sa.ForeignKey("product_category.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    seo_description = sa.Column(sa.String(300))
    seo_title = sa.Column(sa.String(70))
    charge_taxes = sa.Column(sa.Boolean, nullable=False)
    weight = sa.Column(sa.Float(53))
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    default_variant_id = sa.Column(
        sa.ForeignKey(
            "product_productvariant.id", deferrable=True, initially="DEFERRED"
        ),
        unique=True,
    )
    description_plaintext = sa.Column(sa.Text, nullable=False)
    search_vector = sa.Column(TSVECTOR, index=True)
    rating = sa.Column(sa.Float(53))

    category = relationship("ProductCategory")
    default_variant = relationship(
        "ProductProductvariant",
        uselist=False,
        primaryjoin="ProductProduct.default_variant_id == ProductProductvariant.id",
    )
    product_type = relationship("ProductProducttype")


class ProductVariant(Model):
    __tablename__ = "product_variant"

    id = sa.Column(sa.Integer, primary_key=True)
    sku = sa.Column(sa.String(255), nullable=False, unique=True)
    name = sa.Column(sa.String(255), nullable=False)
    product_id = sa.Column(
        sa.ForeignKey("product_product.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    track_inventory = sa.Column(sa.Boolean, nullable=False)
    weight = sa.Column(sa.Float(53))
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    sort_order = sa.Column(sa.Integer, index=True)

    product = relationship(
        "ProductProduct",
        primaryjoin="ProductProductvariant.product_id == ProductProduct.id",
    )


class CollectionProduct(Model):
    __tablename__ = "collection_product"
    __table_args__ = (sa.UniqueConstraint("collection_id", "product_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    collection_id = sa.Column(
        sa.ForeignKey("product_collection.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    product_id = sa.Column(
        sa.ForeignKey("product_product.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    sort_order = sa.Column(sa.Integer, index=True)

    collection = relationship("ProductCollection")
    product = relationship("ProductProduct")


class ProductDigitalContent(Model):
    __tablename__ = "product_digital_content"

    id = sa.Column(sa.Integer, primary_key=True)
    use_default_settings = sa.Column(sa.Boolean, nullable=False)
    automatic_fulfillment = sa.Column(sa.Boolean, nullable=False)
    content_type = sa.Column(sa.String(128), nullable=False)
    content_file = sa.Column(sa.String(100), nullable=False)
    max_downloads = sa.Column(sa.Integer)
    url_valid_days = sa.Column(sa.Integer)
    product_variant_id = sa.Column(
        sa.ForeignKey(
            "product_productvariant.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        unique=True,
    )
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)

    product_variant = relationship("ProductProductvariant", uselist=False)


class ProductMedia(Model):
    __tablename__ = "product_media"

    id = sa.Column(sa.Integer, primary_key=True)
    sort_order = sa.Column(sa.Integer, index=True)
    image = sa.Column(sa.String(100))
    ppoi = sa.Column(sa.String(20), nullable=False)
    alt = sa.Column(sa.String(128), nullable=False)
    type = sa.Column(sa.String(32), nullable=False)
    external_url = sa.Column(sa.String(256))
    oembed_data = sa.Column(JSONB, nullable=False)
    product_id = sa.Column(
        sa.ForeignKey("product_product.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    product = relationship("ProductProduct")


class ProductTranslation(Model):
    __tablename__ = "product_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "product_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    seo_title = sa.Column(sa.String(70))
    seo_description = sa.Column(sa.String(300))
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(250))
    description = sa.Column(JSONB)
    product_id = sa.Column(
        sa.ForeignKey("product_product.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    product = relationship("ProductProduct")


class ProductVariantTranslation(Model):
    __tablename__ = "product_variant_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "product_variant_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(255), nullable=False)
    product_variant_id = sa.Column(
        sa.ForeignKey(
            "product_productvariant.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )

    product_variant = relationship("ProductProductvariant")


class ProductDigitalContentUrl(Model):
    __tablename__ = "product_digital_content_url"

    id = sa.Column(sa.Integer, primary_key=True)
    token = sa.Column(UUID, nullable=False, unique=True)
    created = sa.Column(sa.DateTime(True), nullable=False)
    download_num = sa.Column(sa.Integer, nullable=False)
    content_id = sa.Column(
        sa.ForeignKey(
            "product_digitalcontent.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    line_id = sa.Column(
        sa.ForeignKey("order_orderline.id", deferrable=True, initially="DEFERRED"),
        unique=True,
    )

    content = relationship("ProductDigitalcontent")
    line = relationship("OrderOrderline", uselist=False)
