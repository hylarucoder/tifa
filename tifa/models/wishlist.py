import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.product import Product, ProductVariant
from tifa.models.user import User
from tifa.models.utils import TimestampMixin


class Wishlist(TimestampMixin, Model):
    __tablename__ = "wishlist"

    id = sa.Column(sa.Integer, primary_key=True)
    token = sa.Column(UUID, nullable=False, unique=True)
    user_id = sa.Column(
        sa.ForeignKey("user.id"),
        unique=True,
    )

    user = relationship(User, uselist=False)


class WishlistItem(TimestampMixin, Model):
    __tablename__ = "wishlist_item"
    __table_args__ = (sa.UniqueConstraint("wishlist_id", "product_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    product_id = sa.Column(
        sa.ForeignKey("product.id"),
        nullable=False,
    )
    product = relationship(Product)
    wishlist_id = sa.Column(
        sa.ForeignKey("wishlist.id"),
        nullable=False,
    )
    wishlist = relationship(Wishlist)


class WishlistItemVariant(TimestampMixin, Model):
    __tablename__ = "wishlist_item_variant"
    __table_args__ = (sa.UniqueConstraint("wishlist_item_id", "product_variant_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    wishlist_item_id = sa.Column(
        sa.ForeignKey("wishlist_item.id"),
        nullable=False,
    )
    product_variant_id = sa.Column(
        sa.ForeignKey("product_variant.id"),
        nullable=False,
    )

    product_variant = relationship(ProductVariant)
    wishlist_item = relationship(WishlistItem)
