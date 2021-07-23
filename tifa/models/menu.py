import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class Menu(Model):
    __tablename__ = "menu_menu"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)


class MenuItemTranslation(Model):
    __tablename__ = "menu_menu_item_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "menu_item_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(128), nullable=False)
    menu_item_id = sa.Column(
        sa.ForeignKey("menu_menuitem.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    menu_item = relationship("MenuMenuitem")


class Menuitem(Model):
    __tablename__ = "menu_menuitem"
    __table_args__ = (
        sa.CheckConstraint("level >= 0"),
        sa.CheckConstraint("lft >= 0"),
        sa.CheckConstraint("rght >= 0"),
        sa.CheckConstraint("tree_id >= 0"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(128), nullable=False)
    sort_order = sa.Column(sa.Integer, index=True)
    url = sa.Column(sa.String(256))
    lft = sa.Column(sa.Integer, nullable=False)
    rght = sa.Column(sa.Integer, nullable=False)
    tree_id = sa.Column(sa.Integer, nullable=False, index=True)
    level = sa.Column(sa.Integer, nullable=False)
    category_id = sa.Column(
        sa.ForeignKey("product_category.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    collection_id = sa.Column(
        sa.ForeignKey("product_collection.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    menu_id = sa.Column(
        sa.ForeignKey("menu_menu.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    page_id = sa.Column(
        sa.ForeignKey("page_page.id", deferrable=True, initially="DEFERRED"), index=True
    )
    parent_id = sa.Column(
        sa.ForeignKey("menu_menuitem.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)

    category = relationship("ProductCategory")
    collection = relationship("ProductCollection")
    menu = relationship("MenuMenu")
    page = relationship("PagePage")
    parent = relationship("MenuMenuitem", remote_side=[id])
