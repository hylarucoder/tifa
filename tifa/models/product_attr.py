import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model


class AttributeAttributeproduct(Model):
    __tablename__ = "attribute_attributeproduct"
    __table_args__ = (sa.UniqueConstraint("attribute_id", "product_type_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    attribute_id = sa.Column(
        sa.ForeignKey("attribute_attribute.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    product_type_id = sa.Column(
        sa.ForeignKey("product_producttype.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    sort_order = sa.Column(sa.Integer, index=True)

    attribute = relationship("AttributeAttribute")
    product_type = relationship("ProductProducttype")


class AttributeAttributevariant(Model):
    __tablename__ = "attribute_attributevariant"
    __table_args__ = (sa.UniqueConstraint("attribute_id", "product_type_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    attribute_id = sa.Column(
        sa.ForeignKey("attribute_attribute.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    product_type_id = sa.Column(
        sa.ForeignKey("product_producttype.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    sort_order = sa.Column(sa.Integer, index=True)

    attribute = relationship("AttributeAttribute")
    product_type = relationship("ProductProducttype")


class ProductVariantmedia(Model):
    __tablename__ = "product_variantmedia"
    __table_args__ = (sa.UniqueConstraint("variant_id", "media_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    media_id = sa.Column(
        sa.ForeignKey("product_productmedia.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    variant_id = sa.Column(
        sa.ForeignKey(
            "product_productvariant.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )

    media = relationship("ProductProductmedia")
    variant = relationship("ProductProductvariant")


class AttributeAssignedproductattributevalue(Model):
    __tablename__ = "attribute_assignedproductattributevalue"
    __table_args__ = (sa.UniqueConstraint("value_id", "assignment_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sort_order = sa.Column(sa.Integer, index=True)
    assignment_id = sa.Column(
        sa.ForeignKey(
            "attribute_assignedproductattribute.id",
            deferrable=True,
            initially="DEFERRED",
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

    assignment = relationship("AttributeAssignedproductattribute")
    value = relationship("AttributeAttributevalue")


class AttributeAssignedvariantattributevalue(Model):
    __tablename__ = "attribute_assignedvariantattributevalue"
    __table_args__ = (sa.UniqueConstraint("value_id", "assignment_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    sort_order = sa.Column(sa.Integer, index=True)
    assignment_id = sa.Column(
        sa.ForeignKey(
            "attribute_assignedvariantattribute.id",
            deferrable=True,
            initially="DEFERRED",
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

    assignment = relationship("AttributeAssignedvariantattribute")
    value = relationship("AttributeAttributevalue")


class AttributeAssignedproductattribute(Model):
    __tablename__ = "attribute_assignedproductattribute"
    __table_args__ = (sa.UniqueConstraint("product_id", "assignment_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    product_id = sa.Column(
        sa.ForeignKey("product_product.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    assignment_id = sa.Column(
        sa.ForeignKey(
            "attribute_attributeproduct.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )

    assignment = relationship("AttributeAttributeproduct")
    product = relationship("ProductProduct")


class AttributeAssignedvariantattribute(Model):
    __tablename__ = "attribute_assignedvariantattribute"
    __table_args__ = (sa.UniqueConstraint("variant_id", "assignment_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    variant_id = sa.Column(
        sa.ForeignKey(
            "product_productvariant.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )
    assignment_id = sa.Column(
        sa.ForeignKey(
            "attribute_attributevariant.id", deferrable=True, initially="DEFERRED"
        ),
        nullable=False,
        index=True,
    )

    assignment = relationship("AttributeAttributevariant")
    variant = relationship("ProductProductvariant")
