from enum import auto

import sqlalchemy as sa
from fastapi_utils.enums import StrEnum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class Attribute(Model):
    __tablename__ = "attribute"

    id = sa.Column(sa.Integer, primary_key=True)
    slug = sa.Column(sa.String(250), nullable=False, unique=True)
    name = sa.Column(sa.String(255), nullable=False)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)

    class InputType(StrEnum):
        DROPDOWN = "dropdown"
        MULTISELECT = "multiselect"
        FILE = "file"
        REFERENCE = "reference"
        NUMERIC = "numeric"
        RICH_TEXT = "rich-text"
        BOOLEAN = "boolean"
        DATE = "date"
        DATE_TIME = "date-time"

        CHOICES = [
            (DROPDOWN, "Dropdown"),
            (MULTISELECT, "Multi Select"),
            (FILE, "File"),
            (REFERENCE, "Reference"),
            (NUMERIC, "Numeric"),
            (RICH_TEXT, "Rich Text"),
            (BOOLEAN, "Boolean"),
            (DATE, "Date"),
            (DATE_TIME, "Date Time"),
        ]

        ALLOWED_IN_VARIANT_SELECTION = [
            DROPDOWN,
            BOOLEAN,
        ]

        TYPES_WITH_CHOICES = [
            DROPDOWN,
            MULTISELECT,
        ]

        TYPES_WITH_UNIQUE_VALUES = [FILE, REFERENCE, RICH_TEXT, NUMERIC, DATE, DATE_TIME]

    input_type = sa.Column(sa.String(50), nullable=False)
    available_in_grid = sa.Column(sa.Boolean, nullable=False, default=True)
    visible_in_storefront = sa.Column(sa.Boolean, nullable=False, default=False)
    filterable_in_dashboard = sa.Column(sa.Boolean, nullable=False)
    filterable_in_storefront = sa.Column(sa.Boolean, nullable=False)
    value_required = sa.Column(sa.Boolean, nullable=False, default=False)
    storefront_search_position = sa.Column(sa.Integer, nullable=False, default=False)
    is_variant_only = sa.Column(sa.Boolean, nullable=False)

    class Type(StrEnum):
        PRODUCT = auto()
        PAGE = auto()

    type = sa.Column(sa.String(50), nullable=False)
    entity_type = sa.Column(sa.String(50))
    unit = sa.Column(sa.String(100))


class AttributeTranslation(Model):
    __tablename__ = "attribute_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "attribute_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(100), nullable=False)
    attribute_id = sa.Column(
        sa.ForeignKey("attribute.id"),
        nullable=False,
        index=True,
    )

    attribute = relationship(Attribute)


class AttributeValue(Model):
    __tablename__ = "attribute_value"
    __table_args__ = (
        sa.UniqueConstraint("slug", "attribute_id"),
        sa.Index("idx_attribute_value_name_slug", "name", "slug"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    attribute_id = sa.Column(sa.ForeignKey("attribute.id"), nullable=False)
    attribute = relationship(Attribute)

    name = sa.Column(sa.String(250), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False, index=True)
    sort_order = sa.Column(sa.Integer, index=True)
    value = sa.Column(sa.String(100), nullable=False)
    content_type = sa.Column(sa.String(50))
    file_url = sa.Column(sa.String(200))
    rich_text = sa.Column(JSONB)
    boolean = sa.Column(sa.Boolean)


class AttributeValueTranslation(Model):
    __tablename__ = "attribute_value_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "attribute_value_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    name = sa.Column(sa.String(100), nullable=False)
    attribute_value_id = sa.Column(sa.ForeignKey("attribute_value.id"), nullable=False)
    rich_text = sa.Column(JSONB)
    attribute_value = relationship(AttributeValue)
