"""
collectionChannelListingUpdate(...): CollectionChannelListingUpdate
"""
from fastapi import Depends
from fastapi_utils.api_model import APIModel

from tifa.apps.admin import bp
from tifa.apps.deps import get_dal
from tifa.db.dal import Dal
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
def categories_page(dal: Dal = Depends(get_dal)):
    return dal.page(ProductCategory)


@bp.item("/category/{id}", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_item(id: str, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(ProductCategory, id)
    return {"item": item}


class ParamsCategoryCreate(APIModel):
    name: str


@bp.op("/category/create", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_create(params: ParamsCategoryCreate, dal: Dal = Depends(get_dal)):
    item = dal.add(ProductCategory, **params.dict())
    return {"item": item}


class ParamsCategoryUpdate(APIModel):
    id: str
    name: str


@bp.op("/category/update", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_update(params: ParamsCategoryUpdate, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(ProductCategory, params.id)
    item.name = params.name
    dal.commit()
    return {"item": item}


class ParamsCategoryDelete(APIModel):
    id: str


@bp.op("/category/delete", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_delete(params: ParamsCategoryDelete, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(ProductCategory, params.id)
    dal.delete(item)
    dal.commit()
    return {"item": item}


class ParamsCategoryBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/category/bulk_delete", out=TCategory, summary="Category", tags=["ProductCategory"]
)
def category_bulk_delete(params: ParamsCategoryBulkDelete, dal: Dal = Depends(get_dal)):
    items = dal.bulk_get(ProductCategory, params.ids)
    for item in items:
        dal.delete(item)
    dal.commit()
    return {"items": items}


class ParamsCategoryTranslate(APIModel):
    id: str
    name: str


@bp.op(
    "/category/translate", out=TCategory, summary="Category", tags=["ProductCategory"]
)
def category_translate(params: ParamsCategoryTranslate, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(ProductCategory, params.id)
    return {"item": item}


class TCollection(APIModel):
    id: str
    name: str


@bp.page(
    "/collections", out=TCollection, summary="Collection", tags=["ProductCollection"]
)
def collections_page(dal: Dal = Depends(get_dal)):
    return dal.page(ProductCollection)


@bp.item(
    "/collection/{id}",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
def collection_item(id: str, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(id)
    return {"item": item}


class ParamsCollectionCreate(APIModel):
    name: str


@bp.op(
    "/collection/create",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
def collection_create(params: ParamsCollectionCreate, dal: Dal = Depends(get_dal)):
    item = dal.add(ProductCollection, **params.dict())
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
def collection_update(params: ParamsCollectionUpdate, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(ProductCollection, params.id)
    return {"item": item}


class ParamsCollectionDelete(APIModel):
    id: str


@bp.op(
    "/collection/delete",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
def collection_delete(params: ParamsCollectionDelete, dal: Dal = Depends(get_dal)):
    item = dal.get_or_404(ProductCollection, params.id)
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
    params: ParamsCollectionBulkDelete, dal: Dal = Depends(get_dal)
):
    items = dal.bulk_get(ProductCollection, params.ids)
    for item in items:
        dal.delete(item)
    dal.commit()
    return {"items": items}


@bp.op(
    "/collection/translate",
    out=TCollection,
    summary="Translate",
    tags=["ProductCollection"],
)
def collection_translate(dal: Dal = Depends(get_dal)):
    item = dal.first_or_404(ProductCollection)
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
    params: ParamsCollectionAddProducts, dal: Dal = Depends(get_dal)
):
    item = dal.get_or_404(ProductCollection, params.id)
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
    params: ParamsCollectionRemoveProducts, dal: Dal = Depends(get_dal)
):
    item = dal.get_or_404(ProductCollection, params.id)
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
    params: ParamsCollectionReorderProducts, dal: Dal = Depends(get_dal)
):
    item = dal.get_or_404(ProductCollection, params.id)
    return {"item": item}
