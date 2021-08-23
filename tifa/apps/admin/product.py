"""
productVariantChannelListingUpdate(...): ProductVariantChannelListingUpdate
productChannelListingUpdate(...): ProductChannelListingUpdate
"""
import datetime
from enum import auto
from typing import Optional

import pydantic as pt
from fastapi_utils.api_model import APIModel
from fastapi_utils.enums import StrEnum

from tifa.apps.admin.local import g
from tifa.apps.admin.router import bp
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
async def product_types_page():
    return await g.adal.page(ProductType)


@bp.item(
    "/product_type/{id}", out=TProductType, summary="ProductType", tags=["ProductType"]
)
async def product_type_item(
    id: str,
):
    item = g.adal.get_or_404(ProductType, id)
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
async def product_type_create(
    params: ParamsProductTypeCreate,
):
    item = g.adal.add(ProductType, **params.dict())
    g.adal.commit()
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
async def product_type_update(
    params: ParamsProductTypeUpdate,
):
    item = g.adal.get_or_404(ProductType, params.id)
    item.name = params.name
    item.has_variants = params.has_variants
    item.is_shipping_required = params.is_shipping_required
    item.is_digital = params.is_digital
    item.weight = params.weight
    item.slug = params.slug
    item.metadata_public = params.metadata_public
    item.metadata_private = params.metadata_private
    g.adal.commit()
    return {"item": item}


class ParamsProductTypeDelete(APIModel):
    id: str


@bp.op(
    "/product_type/delete",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
async def product_type_delete(
    params: ParamsProductTypeDelete,
):
    item = g.adal.get_or_404(ProductType, params.id)
    g.adal.delete(item)
    g.adal.commit()
    return {"item": item}


class ParamsProductTypeBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/product_type/bulk_delete",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
async def product_type_bulk_delete(
    params: ParamsProductTypeBulkDelete,
):
    items = g.adal.bulk_get(ProductType, params.ids)
    for item in items:
        # soft vs hard
        g.adal.delete(item)
    await g.adal.commit()
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
async def product_type_assign_attributes(
    params: ParamsProductTypeAssignAttributes,
):
    item = await g.adal.get_or_404(ProductType, params.id)
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
async def product_type_unassign_attributes(
    params: ParamsProductTypeUnassignAttributes,
):
    item = await g.adal.get_or_404(ProductType, params.id)
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
async def product_type_reorder_attributes(
    params: ParamsProductTypeReorderAttributes,
):
    item = await g.adal.get_or_404(ProductType, params.id)
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
async def products_page():
    return await g.adal.page(Product)


@bp.item("/product/{id}", out=TProduct, summary="Product", tags=["Product"])
async def get_product(
    id: str,
):
    item = await g.adal.get_or_404(Product, id)
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
async def product_create(
    params: ParamsProductCreate,
):
    item = await g.adal.add(Product, **params.dict())
    g.adal.commit()
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
async def product_update(
    params: ParamsProductUpdate,
):
    item = await g.adal.get_or_404(Product, params.id)
    return {"item": item}


class ParamsProductDelete(APIModel):
    id: str


@bp.op("/product/delete", out=TProduct, summary="Product", tags=["Product"])
async def product_delete(
    params: ParamsProductDelete,
):
    item = await g.adal.get_or_404(Product, params.id)
    return {"item": item}


class ParamsProductBulkDelete(APIModel):
    ids: list[str]


@bp.op("/product/bulk_delete", out=TProduct, summary="Product", tags=["Product"])
async def product_bulk_delete(
    params: ParamsProductBulkDelete,
):
    items = await g.adal.bulk_get(Product, params.ids)
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
async def product_reorder_attribute_values(
    params: ParamsProductReorderAttributeValues,
):
    item = await g.adal.get_or_404(Product, params.id)
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
async def get_product_variants():
    return await g.adal.page(ProductVariant)


@bp.item(
    "/product_variant/{id}",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def get_product_variant(
    id: str,
):
    item = await g.adal.get_or_404(ProductVariant, id)
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
async def product_variant_create(
    params: ParamsProductVariantCreate,
):
    item = await g.adal.add(ProductVariant)
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
async def product_variant_bulk_create(
    params: ParamsProductVariantBulkCreate,
):
    """
    TODO: no variants
    """
    item = await g.adal.first_or_404(ProductVariant)
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
async def product_variant_update(
    params: ParamsProductVariantUpdate,
):
    item = await g.adal.get_or_404(ProductVariant, params.id)
    return {"item": item}


class ParamsProductVariantDelete(APIModel):
    id: str


@bp.op(
    "/product_variant/delete",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_delete(
    params: ParamsProductVariantDelete,
):
    item = await g.adal.get_or_404(ProductVariant, params.id)
    return {"item": item}


class ParamsProductVariantBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/product_variant/bulk_delete",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_bulk_delete(
    params: ParamsProductVariantBulkDelete,
):
    items = await g.adal.bulk_get(ProductVariant, params.ids)
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
async def product_variant_reorder(
    params: ParamsProductVariantReorder,
):
    items = await g.adal.bulk_get(ProductVariant, params.ids)
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
async def product_variant_reorder_attribute_values(
    params: ParamsProductVariantReorderAttributeValues,
):
    item = await g.adal.get_or_404(ProductVariant, params.id)
    return {"item": item}


@bp.op(
    "/product_variant/translate",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_translate():
    item = await g.adal.first_or_404(ProductVariant)
    return {"item": item}


class ParamsProductVariantSetDefault(APIModel):
    id: str


@bp.op(
    "/product_variant/set_default",
    out=TProductVariant,
    summary="ProductVariant-set default",
    tags=["ProductVariant"],
)
async def product_variant_set_default(
    params: ParamsProductVariantSetDefault,
):
    item = await g.adal.get_or_404(ProductVariant, params.id)
    return {"item": item}


@bp.op(
    "/product_variant/stocks/create",
    out=TProductVariant,
    summary="ProductVariant-stocks-create",
    tags=["ProductVariant"],
)
async def product_variant_stocks_create():
    item = await g.adal.first_or_404(ProductVariant)
    return {"item": item}


@bp.op(
    "/product_variant/stocks/update",
    out=TProductVariant,
    summary="ProductVariant-stocks-update",
    tags=["ProductVariant"],
)
async def product_variant_stocks_update():
    item = await g.adal.first_or_404(ProductVariant)
    return {"item": item}


@bp.op(
    "/product_variant/stocks/delete",
    out=TProductVariant,
    summary="ProductVariant-stocks-update",
    tags=["ProductVariant"],
)
async def product_variant_stocks_delete():
    item = await g.adal.first_or_404(ProductVariant)
    return {"item": item}
