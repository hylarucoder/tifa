"""
productAttributeAssign(...): ProductAttributeAssign
productAttributeUnassign(...): ProductAttributeUnassign

productVariantChannelListingUpdate(...): ProductVariantChannelListingUpdate
productChannelListingUpdate(...): ProductChannelListingUpdate
"""

from fastapi_utils.api_model import APIModel

from tifa.apps.admin import bp
from tifa.globals import db
from tifa.db.dal import Dal
from tifa.models.menu import Menu
from tifa.models.product import ProductType


class TProductType(APIModel):
    id: str
    name: str
    has_variants: bool
    is_shipping_required: bool
    weight: bool
    is_digital: bool
    metadata_public: bool
    metadata_private: bool
    slug: str


@bp.page(
    "/product_types", out=TProductType, summary="ProductType", tags=["ProductType"]
)
def product_types_page():
    adal = Dal(db.session)
    merchant = adal.first_or_404(ProductType)
    return {"items": merchant}


@bp.item(
    "/product_type/{id}", out=TProductType, summary="ProductType", tags=["ProductType"]
)
def product_type_item(id: str):
    adal = Dal(db.session)
    merchant = adal.get_or_404(ProductType, id)
    return {"item": merchant}


class ParamsProductTypeCreate(APIModel):
    name: str
    has_variants: bool
    is_shipping_required: bool
    weight: bool
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
def product_type_create(params: ParamsProductTypeCreate):
    adal = Dal(db.session)
    item = adal.add(
        ProductType,
    )
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
def product_type_update(params: ParamsProductTypeUpdate):
    adal = Dal(db.session)
    item = adal.add(
        ProductType,
    )
    return {"item": item}


class ParamsProductTypeDelete(APIModel):
    id: str


@bp.op(
    "/product_type/delete",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
def product_type_delete(params: ParamsProductTypeDelete):
    adal = Dal(db.session)
    merchant = adal.get_or_404(ProductType, params.id)
    return {"item": merchant}


class ParamsProductTypeBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/product_type/bulk_delete",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
def product_type_bulk_delete(params: ParamsProductTypeBulkDelete):
    adal = Dal(db.session)
    items = adal.bulk_get(ProductType, params.ids)
    for item in items:
        # soft vs hard
        adal.delete(item)
    adal.commit()
    return {"items": items}


class ParamsProductTypeReorderAttributes(APIModel):
    id: str
    attr_ids: list[str]


@bp.op(
    "/product_type/reorder_attributes",
    out=TProductType,
    summary="ProductType-reorder_attributes",
    tags=["ProductType"],
)
def product_type_reorder_attributes():
    adal = Dal(db.session)
    item = adal.first_or_404(ProductType)
    return {"item": item}


class TProduct(APIModel):
    id: str
    name: str
    description: dict

@bp.list("/products", out=TProduct, summary="Product", tags=["Product"])
def get_products():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"items": merchant}


@bp.item("/product", out=TProduct, summary="Product", tags=["Product"])
def get_product():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/product/create", out=TProduct, summary="Product", tags=["Product"])
def product_create():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/product/update", out=TProduct, summary="Product", tags=["Product"])
def product_update():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/product/delete", out=TProduct, summary="Product", tags=["Product"])
def product_delete():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/product/bulk_delete", out=TProduct, summary="Product", tags=["Product"])
def product_bulk_delete():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/product/translate", out=TProduct, summary="Product", tags=["Product"])
def product_translate():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product/reorder_attribute_values",
    out=TProduct,
    summary="Product-reorder_attribute_values",
    tags=["Product"],
)
def product_reorder_attribute_values():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


class TProductVariant(APIModel):
    id: str
    name: str


@bp.list(
    "/product_variants",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def get_product_variants():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.item(
    "/product_variant",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def get_product_variant():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/create",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_create():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/bulk_create",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_bulk_create():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/update",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_update():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/delete",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_delete():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/bulk_delete",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_bulk_delete():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/reorder",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_reorder():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/reorder_attribute_values",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_reorder_attribute_values():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/translate",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
def product_variant_translate():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/set_default",
    out=TProductVariant,
    summary="ProductVariant-set default",
    tags=["ProductVariant"],
)
def product_variant_set_default():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/stocks/create",
    out=TProductVariant,
    summary="ProductVariant-stocks-create",
    tags=["ProductVariant"],
)
def product_variant_stocks_create():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/stocks/update",
    out=TProductVariant,
    summary="ProductVariant-stocks-update",
    tags=["ProductVariant"],
)
def product_variant_stocks_update():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/stocks/delete",
    out=TProductVariant,
    summary="ProductVariant-stocks-update",
    tags=["ProductVariant"],
)
def product_variant_stocks_delete():
    adal = Dal(db.session)
    merchant = adal.first_or_404(Menu)
    return {"item": merchant}
