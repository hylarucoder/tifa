import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.utils import TimestampMixin, MetadataMixin


class ProductCollection(MetadataMixin, TimestampMixin, Model):
    __tablename__ = "product_collection"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False, unique=True)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    description = sa.Column(JSONB)
    seo_description = sa.Column(sa.String(300))
    seo_title = sa.Column(sa.String(70))
    background_image = sa.Column(sa.String(100))
    background_image_alt = sa.Column(sa.String(128), nullable=False)


class ProductCategory(MetadataMixin, TimestampMixin, Model):
    __tablename__ = "product_category"

    id = sa.Column(sa.Integer, primary_key=True)
    parent_id = sa.Column(sa.ForeignKey("product_category.id"))
    parent = relationship("ProductCategory", remote_side=[id])

    name = sa.Column(sa.String(250), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    description = sa.Column(JSONB)
    seo_description = sa.Column(sa.String(300))
    seo_title = sa.Column(sa.String(70))
    background_image = sa.Column(sa.String(100))
    background_image_alt = sa.Column(sa.String(128), nullable=False)
