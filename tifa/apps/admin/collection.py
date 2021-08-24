"""
collectionChannelListingUpdate(...): CollectionChannelListingUpdate
"""
from fastapi_utils.api_model import APIModel

from tifa.apps.admin import bp, g
from tifa.models.product_collection import ProductCategory, ProductCollection


class TCategory(APIModel):
    id: str
    name: str
    slug: str
    description: dict
    level: int
    seo_description: str
    seo_title: str
    background_image: str
    background_image_alt: str
    metadata_public: dict
    metadata_private: dict


@bp.page("/categories", out=TCategory, summary="Category", tags=["ProductCategory"])
def categories_page():
    return g.adal.page(ProductCategory)


@bp.item("/category/{id}", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_item(
    id: str,
):
    item = g.adal.get_or_404(ProductCategory, id)
    return {"item": item}


class ParamsCategoryCreate(APIModel):
    name: str


@bp.op("/category/create", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_create(
    params: ParamsCategoryCreate,
):
    item = g.adal.add(ProductCategory, **params.dict())
    return {"item": item}


class ParamsCategoryUpdate(APIModel):
    id: str
    name: str


@bp.op("/category/update", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_update(
    params: ParamsCategoryUpdate,
):
    item = g.adal.get_or_404(ProductCategory, params.id)
    item.name = params.name
    adal.commit()
    return {"item": item}


class ParamsCategoryDelete(APIModel):
    id: str


@bp.op("/category/delete", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_delete(
    params: ParamsCategoryDelete,
):
    item = g.adal.get_or_404(ProductCategory, params.id)
    g.adal.delete(item)
    g.adal.commit()
    return {"item": item}


class ParamsCategoryBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/category/bulk_delete", out=TCategory, summary="Category", tags=["ProductCategory"]
)
def category_bulk_delete(
    params: ParamsCategoryBulkDelete,
):
    items = g.adal.bulk_get(ProductCategory, params.ids)
    for item in items:
        g.adal.delete(item)
    g.adal.commit()
    return {"items": items}


class ParamsCategoryTranslate(APIModel):
    id: str
    name: str


@bp.op(
    "/category/translate", out=TCategory, summary="Category", tags=["ProductCategory"]
)
def category_translate(
    params: ParamsCategoryTranslate,
):
    item = g.adal.get_or_404(ProductCategory, params.id)
    return {"item": item}


class TCollection(APIModel):
    id: str
    name: str


@bp.page(
    "/collections", out=TCollection, summary="Collection", tags=["ProductCollection"]
)
def collections_page():
    return g.adal.page(ProductCollection)


@bp.item(
    "/collection/{id}",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
def collection_item(
    id: str,
):
    item = g.adal.get_or_404(id)
    return {"item": item}


class ParamsCollectionCreate(APIModel):
    name: str


@bp.op(
    "/collection/create",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
def collection_create(
    params: ParamsCollectionCreate,
):
    item = g.adal.add(ProductCollection, **params.dict())
    return {"item": item}


class ParamsCollectionUpdate(APIModel):
    id: str
    name: str


@bp.op(
    "/collection/update",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
def collection_update(
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
def collection_delete(
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
def collection_bulk_delete(
    params: ParamsCollectionBulkDelete,
):
    items = g.adal.bulk_get(ProductCollection, params.ids)
    for item in items:
        g.adal.delete(item)
    g.adal.commit()
    return {"items": items}


@bp.op(
    "/collection/translate",
    out=TCollection,
    summary="Translate",
    tags=["ProductCollection"],
)
def collection_translate():
    item = g.adal.first_or_404(ProductCollection)
    return {"item": item}


class ParamsCollectionAddProducts(APIModel):
    id: str
    product_ids: list[str]


@bp.op(
    "/collection/add_products",
    out=TCollection,
    summary="AddProducts",
    tags=["ProductCollection"],
)
def collection_add_products(
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
def collection_remove_products(
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
def collection_reorder_products(
    params: ParamsCollectionReorderProducts,
):
    item = g.adal.get_or_404(ProductCollection, params.id)
    return {"item": item}
