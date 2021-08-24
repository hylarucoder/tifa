"""
collectionChannelListingUpdate(...): CollectionChannelListingUpdate
"""
import datetime
from enum import auto
from typing import Union

from fastapi_utils.api_model import APIModel
from fastapi_utils.enums import StrEnum
from pydantic import validator

from tifa.apps.admin import bp, g
from tifa.models.product_collection import ProductCategory, ProductCollection


class TDescBlockHeader(APIModel):
    text: str
    level: int


class TDescBlockParagraph(APIModel):
    text: str


class TDescBlockQuote(APIModel):
    text: str
    caption: str
    alignment: str  # "left/right"


class TDescBlockType(StrEnum):
    PARAGRAPH = auto()
    QUOTE = auto()
    HEADER = auto()


class TDescBlock(APIModel):
    type: TDescBlockType
    data: Union[TDescBlockHeader, TDescBlockParagraph, TDescBlockQuote]


class TCategoryDesc(APIModel):
    blocks: list[TDescBlock]
    time: datetime.datetime
    version: str
    ...


class TCategory(APIModel):
    id: str
    name: str
    slug: str
    description: TCategoryDesc
    seo_description: str
    seo_title: str
    background_image: str
    background_image_alt: str
    metadata_public: dict[str, str]
    metadata_private: dict[str, str]


@bp.page("/categories", out=TCategory, summary="Category", tags=["ProductCategory"])
async def categories_page():
    pagination = await g.adal.page(ProductCategory)
    return pagination


@bp.item("/category/{id}", out=TCategory, summary="Category", tags=["ProductCategory"])
async def category_item(
    id: str,
):
    item = await g.adal.get_or_404(ProductCategory, id)
    return {"item": item}


class BodyCategoryCreate(APIModel):
    name: str
    slug: str
    description: TCategoryDesc
    seo_description: str
    seo_title: str
    background_image: str
    background_image_alt: str
    metadata_public: dict[str, str]
    metadata_private: dict[str, str]

    @validator("name")
    def name_must_contain_space(cls, v):
        return v.title()

    @validator("slug")
    def slug_ensure_and_unique(cls, v):
        print("---->", v)
        return v.title()


@bp.op("/category/create", out=TCategory, summary="Category", tags=["ProductCategory"])
async def category_create(
    body: BodyCategoryCreate,
):
    item = g.adal.add(ProductCategory, **body.dict())
    await g.adal.commit()

    return {"item": item}


class ParamsCategoryUpdate(APIModel):
    id: str
    name: str
    slug: str
    description: TCategoryDesc
    seo_description: str
    seo_title: str
    background_image: str
    background_image_alt: str
    metadata_public: dict[str, str]
    metadata_private: dict[str, str]


@bp.op("/category/update", out=TCategory, summary="Category", tags=["ProductCategory"])
async def category_update(
    params: ParamsCategoryUpdate,
):
    item = await g.adal.get_or_404(ProductCategory, params.id)
    item.name = params.name
    g.adal.commit()
    return {"item": item}


class ParamsCategoryDelete(APIModel):
    id: str


@bp.op("/category/delete", out=TCategory, summary="Category", tags=["ProductCategory"])
async def category_delete(
    params: ParamsCategoryDelete,
):
    item = g.adal.get_or_404(ProductCategory, params.id)
    g.adal.delete(item)
    await g.adal.commit()
    return {"item": item}


class ParamsCategoryBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/category/bulk_delete", out=TCategory, summary="Category", tags=["ProductCategory"]
)
async def category_bulk_delete(
    params: ParamsCategoryBulkDelete,
):
    items = g.adal.bulk_get(ProductCategory, params.ids)
    for item in items:
        g.adal.delete(item)
    g.adal.commit()
    return {"items": items}


class TCollection(APIModel):
    id: str
    name: str


@bp.page(
    "/collections", out=TCollection, summary="Collection", tags=["ProductCollection"]
)
async def collections_page():
    return g.adal.page(ProductCollection)


@bp.item(
    "/collection/{id}",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
async def collection_item(
    id: str,
):
    item = g.adal.get_or_404(id)
    return {"item": item}


class ParamsCollectionCreate(APIModel):
    name: str
    slug: str
    description: TCategoryDesc
    seo_description: str
    seo_title: str
    background_image: str
    background_image_alt: str
    metadata_public: dict[str, str]
    metadata_private: dict[str, str]


@bp.op(
    "/collection/create",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
async def collection_create(
    params: ParamsCollectionCreate,
):
    item = await g.adal.add(ProductCollection, **params.dict())
    return {"item": item}


class ParamsCollectionUpdate(APIModel):
    id: str
    name: str
    description: TCategoryDesc
    seo_description: str
    seo_title: str
    background_image: str
    background_image_alt: str
    metadata_public: dict[str, str]
    metadata_private: dict[str, str]


@bp.op(
    "/collection/update",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
async def collection_update(
    params: ParamsCollectionUpdate,
):
    item = g.adal.get_or_404(ProductCollection, params.id)
    return {"item": item}


class ParamsCollectionDelete(APIModel):
    id: str


@bp.op(
    "/collection/delete",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
async def collection_delete(
    params: ParamsCollectionDelete,
):
    item = g.adal.get_or_404(ProductCollection, params.id)
    return {"item": item}


class ParamsCollectionBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/collection/bulk_delete",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
async def collection_bulk_delete(
    params: ParamsCollectionBulkDelete,
):
    items = g.adal.bulk_get(ProductCollection, params.ids)
    for item in items:
        g.adal.delete(item)
    g.adal.commit()
    return {"items": items}


class ParamsCollectionAddProducts(APIModel):
    id: str
    product_ids: list[str]


@bp.op(
    "/collection/add_products",
    out=TCollection,
    summary="AddProducts",
    tags=["ProductCollection"],
)
async def collection_add_products(
    params: ParamsCollectionAddProducts,
):
    item = g.adal.get_or_404(ProductCollection, params.id)
    return {"item": item}


class ParamsCollectionRemoveProducts(APIModel):
    id: str
    product_ids: list[str]


@bp.op(
    "/collection/remove_products",
    out=TCollection,
    summary="RemoveProducts",
    tags=["ProductCollection"],
)
async def collection_remove_products(
    params: ParamsCollectionRemoveProducts,
):
    item = g.adal.get_or_404(ProductCollection, params.id)
    return {"item": item}


class ParamsCollectionReorderProducts(APIModel):
    id: str
    product_ids: list[str]


@bp.op(
    "/collection/reorder_products",
    out=TCollection,
    summary="ReorderProducts",
    tags=["ProductCollection"],
)
async def collection_reorder_products(
    params: ParamsCollectionReorderProducts,
):
    item = g.adal.get_or_404(ProductCollection, params.id)
    return {"item": item}
