import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.product import ProductVariant, Product


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
    product_id = sa.Column(sa.ForeignKey("product.id"), nullable=False)
    product = relationship(Product)


class ProductVariantMedia(Model):
    __tablename__ = "product_variant_media"
    __table_args__ = (sa.UniqueConstraint("variant_id", "media_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    media_id = sa.Column(
        sa.ForeignKey("product_media.id"),
        nullable=False,
    )
    media = relationship(ProductMedia)
    variant_id = sa.Column(
        sa.ForeignKey("product_variant.id"),
        nullable=False,
    )

    variant = relationship(ProductVariant)
