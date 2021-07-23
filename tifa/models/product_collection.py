import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class ProductCollectionChannelListing(Model):
    __tablename__ = "product_collection_channel_listing"
    __table_args__ = (sa.UniqueConstraint("collection_id", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    publication_date = sa.Column(sa.Date)
    is_published = sa.Column(sa.Boolean, nullable=False)
    channel_id = sa.Column(
        sa.ForeignKey("channel_channel.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    collection_id = sa.Column(
        sa.ForeignKey("product_collection.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    channel = relationship("ChannelChannel")
    collection = relationship("ProductCollection")


class ProductCollection(Model):
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


class ProductCollectionTranslation(Model):
    __tablename__ = "product_collection_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "collection_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    seo_title = sa.Column(sa.String(70))
    seo_description = sa.Column(sa.String(300))
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(128))
    collection_id = sa.Column(
        sa.ForeignKey("product_collection.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    description = sa.Column(JSONB)

    collection = relationship("ProductCollection")
