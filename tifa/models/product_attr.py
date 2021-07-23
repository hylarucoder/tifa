import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.attr import Attribute, AttributeValue
from tifa.models.product import ProductType, Product, ProductVariant


class AttributeProduct(Model):
    __tablename__ = "attribute_product"
    __table_args__ = (sa.UniqueConstraint("attribute_id", "product_type_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    attribute_id = sa.Column(
        sa.ForeignKey("attribute.id"),
        nullable=False,
    )
    attribute = relationship(Attribute)
    product_type_id = sa.Column(
        sa.ForeignKey("product_type.id"),
        nullable=False,
    )
    product_type = relationship(ProductType)
    sort_order = sa.Column(sa.Integer, index=True)


class AssignedProductAttribute(Model):
    __tablename__ = "assigned_product_attribute"
    __table_args__ = (sa.UniqueConstraint("product_id", "assignment_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    product_id = sa.Column(sa.ForeignKey("product.id"), nullable=False)
    product = relationship(Product)
    assignment_id = sa.Column(sa.ForeignKey("attribute_product.id"), nullable=False, )
    assignment = relationship(AttributeProduct)


class AssignedProductAttributeValue(Model):
    __tablename__ = "assigned_product_attribute_value"
    __table_args__ = (sa.UniqueConstraint("value_id", "assignment_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sort_order = sa.Column(sa.Integer, index=True)
    assignment_id = sa.Column(
        sa.ForeignKey("assigned_product_attribute.id"),
        nullable=False,
    )
    assignment = relationship(AssignedProductAttribute)

    value_id = sa.Column(
        sa.ForeignKey("attribute_value.id"),
        nullable=False,
    )
    value = relationship(AttributeValue)


class AttributeVariant(Model):
    __tablename__ = "attribute_variant"
    __table_args__ = (sa.UniqueConstraint("attribute_id", "product_type_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    attribute_id = sa.Column(
        sa.ForeignKey("attribute.id"),
        nullable=False,
    )
    product_type_id = sa.Column(
        sa.ForeignKey("product_type.id"),
        nullable=False,
    )
    sort_order = sa.Column(sa.Integer, index=True)

    attribute = relationship(Attribute)
    product_type = relationship(ProductType)


class AssignedVariantAttribute(Model):
    __tablename__ = "assigned_variant_attribute"
    __table_args__ = (sa.UniqueConstraint("variant_id", "assignment_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    variant_id = sa.Column(
        sa.ForeignKey("product_variant.id"),
        nullable=False,
    )
    assignment_id = sa.Column(
        sa.ForeignKey("attribute_variant.id"),
        nullable=False,
    )

    assignment = relationship(AttributeVariant)
    variant = relationship(ProductVariant)


class AssignedVariantAttributeValue(Model):
    __tablename__ = "assigned_variant_attribute_value"
    __table_args__ = (sa.UniqueConstraint("value_id", "assignment_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sort_order = sa.Column(sa.Integer, index=True)
    assignment_id = sa.Column(sa.ForeignKey("assigned_variant_attribute.id", ), nullable=False)
    assignment = relationship(AssignedVariantAttribute)
    value_id = sa.Column(sa.ForeignKey("attribute_value.id"), nullable=False, )
    value = relationship(AttributeValue)
