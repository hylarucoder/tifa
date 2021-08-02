"""
collectionChannelListingUpdate(...): CollectionChannelListingUpdate
"""
from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, Dal
from ...models.menu import Menu
from ...models.product_collection import ProductCategory


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
    adal = Dal(db.session)
    items = adal.all(ProductCategory)
    return {"items": items}


@bp.item("/category/{id}", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_item(id: str):
    adal = Dal(db.session)
    item = adal.get_or_404(ProductCategory, id)
    return {"item": item}


class ParamsCategoryCreate(APIModel):
    name: str


@bp.op("/category/create", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_create(params: ParamsCategoryCreate):
    adal = Dal(db.session)
    item = adal.add(
        ProductCategory,
        **params.dict()
    )
    return {"item": item}


class ParamsCategoryUpdate(APIModel):
    id: str
    name: str


@bp.op("/category/update", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_update(params: ParamsCategoryUpdate):
    adal = Dal(db.session)
    item = adal.get_or_404(ProductCategory, params.id)
    item.name = params.name
    adal.commit()
    return {"item": item}


class ParamsCategoryDelete(APIModel):
    id: str


@bp.op("/category/delete", out=TCategory, summary="Category", tags=["ProductCategory"])
def category_delete(params: ParamsCategoryDelete):
    adal = Dal(db.session)
    item = adal.get_or_404(ProductCategory, params.id)
    adal.delete(item)
    adal.commit()
    return {"item": item}


class ParamsCategoryBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/category/bulk_delete", out=TCategory, summary="Category", tags=["ProductCategory"]
)
def category_bulk_delete(params: ParamsCategoryBulkDelete):
    adal = Dal(db.session)
    items = adal.bulk_get(ProductCategory, params.ids)
    for item in items:
        adal.delete(item)
    adal.commit()
    return {"items": items}


@bp.op(
    "/category/translate", out=TCategory, summary="Category", tags=["ProductCategory"]
)
def category_translate():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}


class TCollection(APIModel):
    id: str
    name: str


@bp.page(
    "/collections", out=TCollection, summary="Collection", tags=["ProductCollection"]
)
def collections_page():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}


@bp.item(
    "/collection", out=TCollection, summary="Collection", tags=["ProductCollection"]
)
def collection_item():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}


@bp.op(
    "/collection/create",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
def collection_create():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}


@bp.op(
    "/collection/update",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
def collection_update():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}


@bp.op(
    "/collection/delete",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
def collection_delete():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}


@bp.op(
    "/collection/bulk_delete",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
def collection_bulk_delete():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}


@bp.op(
    "/collection/translate",
    out=TCollection,
    summary="Translate",
    tags=["ProductCollection"],
)
def collection_translate():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}


@bp.op(
    "/collection/add_products",
    out=TCollection,
    summary="AddProducts",
    tags=["ProductCollection"],
)
def collection_add_products():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}


@bp.op(
    "/collection/remove_products",
    out=TCollection,
    summary="RemoveProducts",
    tags=["ProductCollection"],
)
def collection_remove_products():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}


@bp.op(
    "/collection/reorder_products",
    out=TCollection,
    summary="ReorderProducts",
    tags=["ProductCollection"],
)
def collection_reorder_products():
    adal = Dal(db.session)
    item = adal.first_or_404(Menu)
    return {"item": item}
