import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.attr import Attribute, AttributeValue
from tifa.models.page import PageType, Page


class AttributePage(Model):
    __tablename__ = "attribute_page"
    __table_args__ = (sa.UniqueConstraint("attribute_id", "page_type_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sort_order = sa.Column(sa.Integer, index=True)
    attribute_id = sa.Column(
        sa.ForeignKey("attribute.id"),
        nullable=False,
    )
    attribute = relationship(Attribute)
    page_type_id = sa.Column(
        sa.ForeignKey("page_type.id"),
        nullable=False,
    )
    page_type = relationship(PageType)


class AssignedPageAttribute(Model):
    __tablename__ = "assigned_page_attribute"

    id = sa.Column(sa.Integer, primary_key=True)
    assignment_id = sa.Column(sa.ForeignKey("attribute_page.id"), nullable=False)
    page_id = sa.Column(sa.ForeignKey("page.id"), nullable=False)

    assignment = relationship(AttributePage)
    page = relationship(Page)


class AssignedPageAttributeValue(Model):
    __tablename__ = "assigned_page_attribute_value"
    __table_args__ = (sa.UniqueConstraint("value_id", "assignment_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sort_order = sa.Column(sa.Integer, index=True)
    assignment_id = sa.Column(sa.ForeignKey("assigned_page_attribute.id"), nullable=False)
    value_id = sa.Column(sa.ForeignKey("attribute_value.id"), nullable=False)
    assignment = relationship(AssignedPageAttribute)
    value = relationship(AttributeValue)
