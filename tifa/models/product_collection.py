import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.utils import TimestampMixin


class ProductCollection(TimestampMixin, Model):
    __tablename__ = "product_collection"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False, unique=True)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    background_image = sa.Column(sa.String(100))
    seo_description = sa.Column(sa.String(300))
    seo_title = sa.Column(sa.String(70))
    description = sa.Column(JSONB)
    background_image_alt = sa.Column(sa.String(128), nullable=False)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)


class ProductCollectionTranslation(TimestampMixin, Model):
    __tablename__ = "product_collection_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "collection_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    seo_title = sa.Column(sa.String(70))
    seo_description = sa.Column(sa.String(300))
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(128))
    collection_id = sa.Column(sa.ForeignKey("product_collection.id"), nullable=False)
    collection = relationship(ProductCollection)
    description = sa.Column(JSONB)


class ProductCategory(TimestampMixin, Model):
    __tablename__ = "product_category"
    __table_args__ = (
        sa.CheckConstraint("level >= 0"),
        sa.CheckConstraint("lft >= 0"),
        sa.CheckConstraint("rght >= 0"),
        sa.CheckConstraint("tree_id >= 0"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    parent_id = sa.Column(sa.ForeignKey("product_category.id"))
    parent = relationship("ProductCategory", remote_side=[id])

    name = sa.Column(sa.String(250), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    description = sa.Column(JSONB)
    lft = sa.Column(sa.Integer, nullable=False)
    rght = sa.Column(sa.Integer, nullable=False)
    tree_id = sa.Column(sa.Integer, nullable=False, index=True)
    level = sa.Column(sa.Integer, nullable=False)
    background_image = sa.Column(sa.String(100))
    seo_description = sa.Column(sa.String(300))
    seo_title = sa.Column(sa.String(70))
    background_image_alt = sa.Column(sa.String(128), nullable=False)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)


class ProductCategoryTranslation(TimestampMixin, Model):
    __tablename__ = "product_category_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "category_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    seo_title = sa.Column(sa.String(70))
    seo_description = sa.Column(sa.String(300))
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(128))
    description = sa.Column(JSONB)
    category_id = sa.Column(sa.ForeignKey("product_category.id"), nullable=False)
    category = relationship(ProductCategory)
