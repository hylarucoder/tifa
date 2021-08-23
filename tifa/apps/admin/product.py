"""
productVariantChannelListingUpdate(...): ProductVariantChannelListingUpdate
productChannelListingUpdate(...): ProductChannelListingUpdate
"""
import datetime
from enum import auto
from typing import Optional

from fastapi import Depends
from fastapi_utils.api_model import APIModel
import pydantic as pt
from fastapi_utils.enums import StrEnum

from tifa.apps.admin import bp
from tifa.apps.deps import get_dal
from tifa.globals import db
from tifa.db.dal import Dal
from tifa.models.product import ProductType, Product, ProductVariant


class TProductType(APIModel):
    id: str
    name: str
    has_variants: bool = pt.Field(title="Product type uses Variant Attributes")
    is_shipping_required: bool
    weight: float
    is_digital: bool
    metadata_public: dict[str, str]
    metadata_private: dict[str, str]
    slug: str


@bp.page(
    "/product_types", out=TProductType, summary="ProductType", tags=["ProductType"]
)
def product_types_page(dal: Dal = Depends(get_dal)):
    return dal.page(ProductType)


@bp.item(
    "/product_type/{id}", out=TProductType, summary="ProductType", tags=["ProductType"]
)
def product_type_item(id: str, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(ProductType, id)
    return {"item": item}


class ParamsProductTypeCreate(APIModel):
    name: str
    has_variants: bool
    is_shipping_required: bool
    weight: float
    is_digital: bool
    metadata_public: dict
    metadata_private: dict
    slug: str


@bp.op(
    "/product_type/create",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
def product_type_create(params: ParamsProductTypeCreate, dal: Dal = Depends(get_dal)):
    item = dal.add(ProductType, **params.dict())
    dal.commit()
    return {"item": item}


class ParamsProductTypeUpdate(APIModel):
    id: str
    name: str
    has_variants: bool
    is_shipping_required: bool
    weight: bool
    is_digital: bool
    metadata_public: dict
    metadata_private: dict
    slug: str


@bp.op(
    "/product_type/update",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
def product_type_update(params: ParamsProductTypeUpdate, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(ProductType, params.id)
    item.name = params.name
    item.has_variants = params.has_variants
    item.is_shipping_required = params.is_shipping_required
    item.is_digital = params.is_digital
    item.weight = params.weight
    item.slug = params.slug
    item.metadata_public = params.metadata_public
    item.metadata_private = params.metadata_private
    dal.commit()
    return {"item": item}


class ParamsProductTypeDelete(APIModel):
    id: str


@bp.op(
    "/product_type/delete",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
def product_type_delete(params: ParamsProductTypeDelete, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(ProductType, params.id)
    dal.delete(item)
    dal.commit()
    return {"item": item}


class ParamsProductTypeBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/product_type/bulk_delete",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
def product_type_bulk_delete(
    params: ParamsProductTypeBulkDelete, dal: Dal = Depends(get_dal)
):
    items = dal.bulk_get(ProductType, params.ids)
    for item in items:
        # soft vs hard
        dal.delete(item)
    dal.commit()
    return {"items": items}


class ParamsProductTypeAssignAttributes(APIModel):
    id: str

    class Type(StrEnum):
        PRODUCT = auto()
        VARIANT = auto()

    type: Type
    attribute_ids: list[str]


@bp.op(
    "/product_type/assign_attributes",
    out=TProductType,
    summary="product_type_assign_attributes",
    tags=["ProductType"],
)
def product_type_assign_attributes(
    params: ParamsProductTypeAssignAttributes, dal: Dal = Depends(get_dal)
):
    item = dal.get_or_404(ProductType, params.id)
    return {"item": item}


class ParamsProductTypeUnassignAttributes(APIModel):
    id: str

    class Type(StrEnum):
        PRODUCT = auto()
        VARIANT = auto()

    type: Type
    attribute_ids: list[str]


@bp.op(
    "/product_type/unassign_attributes",
    out=TProductType,
    summary="product_type_unassign_attributes",
    tags=["ProductType"],
)
def product_type_unassign_attributes(
    params: ParamsProductTypeUnassignAttributes, dal: Dal = Depends(get_dal)
):
    item = dal.get_or_404(ProductType, params.id)
    return {"item": item}


class ParamsProductTypeReorderAttributes(APIModel):
    id: str

    attribute_ids: list[str]


@bp.op(
    "/product_type/reorder_attributes",
    out=TProductType,
    summary="product_type_reorder_attributes",
    tags=["ProductType"],
)
def product_type_reorder_attributes(
    params: ParamsProductTypeReorderAttributes, dal: Dal = Depends(get_dal)
):
    item = dal.get_or_404(ProductType, params.id)
    return {"item": item}


class TProduct(APIModel):
    id: str
    name: str
    description: dict
    description_plaintext: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    product_type: TProductType
    category_id: str
    seo_title: str
    seo_description: str
    charge_taxes: bool
    weight: float
    metadata_public: dict[str, str]
    metadata_private: dict[str, str]
    slug: str

    class Variant(APIModel):
        id: str
        name: str

    variants: list[Variant]
    rating: float


@bp.page("/products", out=TProduct, summary="Product", tags=["Product"])
def products_page(dal: Dal = Depends(get_dal)):
    return dal.page(Product)


@bp.item("/product/{id}", out=TProduct, summary="Product", tags=["Product"])
def get_product(id: str, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(Product, id)
    return {"item": item}


class ParamsProductCreate(APIModel):
    name: str
    description: dict
    description_plaintext: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    product_type_id: str
    category_id: Optional[str]
    seo_title: str
    seo_description: str
    charge_taxes: bool
    weight: float
    metadata_public: dict[str, str]
    metadata_private: dict[str, str]
    slug: str
    rating: float


@bp.op("/product/create", out=TProduct, summary="Product", tags=["Product"])
def product_create(params: ParamsProductCreate, dal: Dal = Depends(get_dal)):
    item = dal.add(Product, **params.dict())
    dal.commit()
    return {"item": item}


class ParamsProductUpdate(APIModel):
    id: str
    name: str
    description: dict
    description_plaintext: str
    category_id: Optional[str]
    collection_ids: list[str]
    seo_title: str
    seo_description: str
    charge_taxes: bool
    weight: float
    metadata_public: dict[str, str]
    metadata_private: dict[str, str]
    slug: str
    rating: float


@bp.op("/product/update", out=TProduct, summary="Product", tags=["Product"])
def product_update(params: ParamsProductUpdate, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(Product, params.id)
    return {"item": item}


class ParamsProductDelete(APIModel):
    id: str


@bp.op("/product/delete", out=TProduct, summary="Product", tags=["Product"])
def product_delete(params: ParamsProductDelete, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(Product, params.id)
    return {"item": item}


class ParamsProductBulkDelete(APIModel):
    ids: list[str]


@bp.op("/product/bulk_delete", out=TProduct, summary="Product", tags=["Product"])
def product_bulk_delete(params: ParamsProductBulkDelete, dal: Dal = Depends(get_dal)):
    items = dal.bulk_get(Product, params.ids)
    return {"items": items}


class ParamsProductReorderAttributeValues(APIModel):
    id: str
    value_ids: list[str]


@bp.op(
    "/product/reorder_attribute_values",
    out=TProduct,
    summary="Product-reorder_attribute_values",
    tags=["Product"],
)
def product_reorder_attribute_values(
    params: ParamsProductReorderAttributeValues, dal: Dal = Depends(get_dal)
):
    item = dal.get_or_404(Product, params.id)
    return {"item": item}


class TProductVariant(APIModel):
    id: str
    name: str


@bp.list(
    "/product_variants",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def get_product_variants(dal: Dal = Depends(get_dal)):
    return dal.page(ProductVariant)


@bp.item(
    "/product_variant/{id}",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def get_product_variant(id: str, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(ProductVariant, id)
    return {"item": item}


class ParamsProductVariantCreate(APIModel):
    product_id: str
    sku: str

    class ItemAttribute(APIModel):
        id: str
        value: str

    attributes: list[ItemAttribute]


@bp.op(
    "/product_variant/create",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_create(
    params: ParamsProductVariantCreate, dal: Dal = Depends(get_dal)
):
    item = dal.add(ProductVariant)
    return {"item": item}


class ParamsProductVariantBulkCreate(APIModel):
    id: str

    class ItemAttribute(APIModel):
        id: str
        value: str

    attributes: list[ItemAttribute]


@bp.op(
    "/product_variant/bulk_create",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_bulk_create(
    params: ParamsProductVariantBulkCreate, dal: Dal = Depends(get_dal)
):
    """
    TODO: no variants
    """
    item = dal.first_or_404(ProductVariant)
    return {"item": item}


class ParamsProductVariantUpdate(APIModel):
    id: str
    sku: str


@bp.op(
    "/product_variant/update",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_update(
    params: ParamsProductVariantUpdate, dal: Dal = Depends(get_dal)
):
    item = dal.get_or_404(ProductVariant, params.id)
    return {"item": item}


class ParamsProductVariantDelete(APIModel):
    id: str


@bp.op(
    "/product_variant/delete",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_delete(
    params: ParamsProductVariantDelete, dal: Dal = Depends(get_dal)
):
    item = dal.get_or_404(ProductVariant, params.id)
    return {"item": item}


class ParamsProductVariantBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/product_variant/bulk_delete",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_bulk_delete(
    params: ParamsProductVariantBulkDelete, dal: Dal = Depends(get_dal)
):
    items = dal.bulk_get(ProductVariant, params.ids)
    return {"items": items}


class ParamsProductVariantReorder(APIModel):
    ids: list[str]
    product_id: str


@bp.op(
    "/product_variant/reorder",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_reorder(
    params: ParamsProductVariantReorder, dal: Dal = Depends(get_dal)
):
    items = dal.bulk_get(ProductVariant, params.ids)
    return {"items": items}


class ParamsProductVariantReorderAttributeValues(APIModel):
    id: str
    value_ids: list[str]


@bp.op(
    "/product_variant/reorder_attribute_values",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_reorder_attribute_values(
    params: ParamsProductVariantReorderAttributeValues, dal: Dal = Depends(get_dal)
):
    item = dal.get_or_404(ProductVariant, params.id)
    return {"item": item}


@bp.op(
    "/product_variant/translate",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_translate():
    adal = Dal(db.session)
    item = adal.first_or_404(ProductVariant)
    return {"item": item}


class ParamsProductVariantSetDefault(APIModel):
    id: str


@bp.op(
    "/product_variant/set_default",
    out=TProductVariant,
    summary="ProductVariant-set default",
    tags=["ProductVariant"],
)
def product_variant_set_default(
    params: ParamsProductVariantSetDefault, dal: Dal = Depends(get_dal)
):
    adal = Dal(db.session)
    item = adal.get_or_404(ProductVariant, params.id)
    return {"item": item}


@bp.op(
    "/product_variant/stocks/create",
    out=TProductVariant,
    summary="ProductVariant-stocks-create",
    tags=["ProductVariant"],
)
def product_variant_stocks_create():
    adal = Dal(db.session)
    item = adal.first_or_404(ProductVariant)
    return {"item": item}


@bp.op(
    "/product_variant/stocks/update",
    out=TProductVariant,
    summary="ProductVariant-stocks-update",
    tags=["ProductVariant"],
)
def product_variant_stocks_update():
    adal = Dal(db.session)
    item = adal.first_or_404(ProductVariant)
    return {"item": item}


@bp.op(
    "/product_variant/stocks/delete",
    out=TProductVariant,
    summary="ProductVariant-stocks-update",
    tags=["ProductVariant"],
)
def product_variant_stocks_delete():
    adal = Dal(db.session)
    item = adal.first_or_404(ProductVariant)
    return {"item": item}
