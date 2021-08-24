import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.utils import MetadataMixin, SortableMixin


class Menu(MetadataMixin, Model):
    __tablename__ = "menu"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(250), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)


class MenuItem(SortableMixin, MetadataMixin, Model):
    __tablename__ = "menu_item"
    __table_args__ = ()

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(128), nullable=False)
    url = sa.Column(sa.String(256))
    category_id = sa.Column(
        sa.ForeignKey("product_category.id"),
    )
    category = relationship("ProductCategory")
    collection_id = sa.Column(
        sa.ForeignKey("product_collection.id"),
    )
    collection = relationship("ProductCollection")
    menu_id = sa.Column(
        sa.ForeignKey("menu.id"),
        nullable=False,
    )
    menu = relationship(Menu)
    page_id = sa.Column(sa.ForeignKey("page.id"))
    page = relationship("Page")
    parent_id = sa.Column(
        sa.ForeignKey("menu_item.id"),
    )
    parent = relationship("MenuItem", remote_side=[id])
