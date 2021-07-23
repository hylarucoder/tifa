import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from tifa.globals import Model


class WishlistWishlistitem(Model):
    __tablename__ = "wishlist_wishlistitem"
    __table_args__ = (sa.UniqueConstraint("wishlist_id", "product_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.DateTime(True), nullable=False)
    product_id = sa.Column(
        sa.ForeignKey("product_product.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    wishlist_id = sa.Column(
        sa.ForeignKey("wishlist_wishlist.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    product = relationship("ProductProduct")
    wishlist = relationship("WishlistWishlist")


class WishlistWishlist(Model):
    __tablename__ = "wishlist_wishlist"

    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.DateTime(True), nullable=False)
    token = sa.Column(UUID, nullable=False, unique=True)
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        unique=True,
    )

    user = relationship("AccountUser", uselist=False)


class WishlistWishlistitemVariant(Model):
    __tablename__ = "wishlist_wishlistitem_variants"
    __table_args__ = (sa.UniqueConstraint("wishlistitem_id", "productvariant_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    wishlistitem_id = sa.Column(
        sa.ForeignKey(
            "wishlist_wishlistitem.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    productvariant_id = sa.Column(
        sa.ForeignKey(
            "product_productvariant.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )

    productvariant = relationship("ProductProductvariant")
    wishlistitem = relationship("WishlistWishlistitem")
