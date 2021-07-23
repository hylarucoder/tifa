import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class PageType(Model):
    __tablename__ = "page_type"
    __table_args__ = (sa.Index("page_pagety_name_7c1cb8_gin", "name", "slug"),)

    id = sa.Column(sa.Integer, primary_key=True)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    name = sa.Column(sa.String(250), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)


class Page(Model):
    __tablename__ = "page"
    __table_args__ = (sa.Index("page_page_title_964714_gin", "title", "slug"),)

    id = sa.Column(sa.Integer, primary_key=True)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    title = sa.Column(sa.String(250), nullable=False)
    content = sa.Column(JSONB)
    created = sa.Column(sa.DateTime(True), nullable=False)
    is_published = sa.Column(sa.Boolean, nullable=False)
    publication_date = sa.Column(sa.Date)
    seo_description = sa.Column(sa.String(300))
    seo_title = sa.Column(sa.String(70))
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    page_type_id = sa.Column(
        sa.ForeignKey("page_pagetype.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    page_type = relationship("PageType")


class AttributeAssignedpageattribute(Model):
    __tablename__ = "attribute_assignedpageattribute"

    id = sa.Column(sa.Integer, primary_key=True)
    assignment_id = sa.Column(
        sa.ForeignKey(
            "attribute_attributepage.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    page_id = sa.Column(
        sa.ForeignKey("page_page.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    assignment = relationship("AttributeAttributepage")
    page = relationship("PagePage")


class PageTranslation(Model):
    __tablename__ = "page_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "page_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    seo_title = sa.Column(sa.String(70))
    seo_description = sa.Column(sa.String(300))
    language_code = sa.Column(sa.String(10), nullable=False)
    title = sa.Column(sa.String(255))
    content = sa.Column(JSONB)
    page_id = sa.Column(
        sa.ForeignKey("page_page.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    page = relationship("Page")


class AttributeAttributepage(Model):
    __tablename__ = "attribute_attributepage"
    __table_args__ = (sa.UniqueConstraint("attribute_id", "page_type_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sort_order = sa.Column(sa.Integer, index=True)
    attribute_id = sa.Column(
        sa.ForeignKey("attribute_attribute.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    page_type_id = sa.Column(
        sa.ForeignKey("page_pagetype.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    attribute = relationship("AttributeAttribute")
    page_type = relationship("PagePagetype")


class AttributeAssignedpageattributevalue(Model):
    __tablename__ = "attribute_assignedpageattributevalue"
    __table_args__ = (sa.UniqueConstraint("value_id", "assignment_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sort_order = sa.Column(sa.Integer, index=True)
    assignment_id = sa.Column(
        sa.ForeignKey(
            "attribute_assignedpageattribute.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    value_id = sa.Column(
        sa.ForeignKey(
            "attribute_attributevalue.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )

    assignment = relationship("AttributeAssignedpageattribute")
    value = relationship("AttributeAttributevalue")
