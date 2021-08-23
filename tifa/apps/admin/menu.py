from fastapi_utils.api_model import APIModel

from tifa.apps.admin.local import g
from tifa.apps.admin.router import bp
from tifa.models.menu import Menu, MenuItem


class TMenu(APIModel):
    id: str
    name: str
    slug: str

    class TItem(APIModel):
        id: str
        name: str

    items: list[TItem]


@bp.page("/menus", out=TMenu, summary="Menu", tags=["Menu"])
async def menus_page():
    items = g.adal.all(Menu)
    return {"items": items}


@bp.item("/menu/{id}", out=TMenu, summary="Menu", tags=["Menu"])
async def menu_item(id: str):
    item = g.adal.get_or_404(Menu, id)
    return {"item": item}


class ParamsMenuCreate(APIModel):
    name: str
    slug: str
    metadata_public: dict
    metadata_private: dict


@bp.op("/menu/create", out=TMenu, summary="Menu", tags=["Menu"])
async def menu_create(params: ParamsMenuCreate):
    item = g.adal.first_or_404(Menu)
    return {"item": item}


class ParamsMenuUpdate(APIModel):
    id: str
    name: str
    slug: str
    metadata_public: dict
    metadata_private: dict


@bp.op("/menu/update", out=TMenu, summary="Menu", tags=["Menu"])
async def menu_update(params: ParamsMenuUpdate):
    item = g.adal.first_or_404(Menu)
    return {"item": item}


class ParamsMenuDelete(APIModel):
    id: str


@bp.op("/menu/delete", out=TMenu, summary="Menu", tags=["Menu"])
async def menu_delete(params: ParamsMenuDelete):
    item = g.adal.first_or_404(Menu)
    return {"item": item}


class ParamsMenuBulkDelete(APIModel):
    ids: list[str]


@bp.op("/menu/bulk_delete", out=TMenu, summary="Menu", tags=["Menu"])
async def menu_bulk_delete(params: ParamsMenuBulkDelete):
    items = g.adal.bulk_get(Menu, params.ids)
    return {"items": items}


class TMenuItem(APIModel):
    id: str
    name: str


class ParamsMenuItems(APIModel):
    menu_id: str


@bp.page("/menu_items", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_items(params: ParamsMenuItems):
    items = g.adal.all(MenuItem, MenuItem.menu_id == params.menu_id)
    return {"items": items}


@bp.item("/menu_item/{id}", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_item(id: str):
    item = g.adal.get_or_404(MenuItem, id)
    return {"item": item}


class ParamsMenuItemCreate(APIModel):
    name: str


@bp.op("/menu_item/create", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_create(params: ParamsMenuItemCreate):
    item = g.adal.add(MenuItem)
    return {"item": item}


class ParamsMenuItemUpdate(APIModel):
    id: str
    name: str


@bp.op("/menu_item/update", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_update(params: ParamsMenuItemUpdate):
    item = g.adal.get_or_404(MenuItem, params.id)
    return {"item": item}


class ParamsMenuItemMove(APIModel):
    id_from: str
    id_to: str


@bp.op("/menu_item/move", out=TMenuItem, summary="MenuItem-Move", tags=["Menu"])
async def menu_item_move(params: ParamsMenuItemMove):
    item_from = g.adal.get_or_404(MenuItem, params.id_from)
    item_to = g.adal.get_or_404(MenuItem, params.id_to)
    return {"item": item_from}


class ParamsMenuItemTranslate(APIModel):
    id: str


@bp.op("/menu_item/translate", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_translate(params: ParamsMenuItemTranslate):
    item = g.adal.get_or_404(MenuItem, params.id)
    return {"item": item}


class ParamsMenuItemDelete(APIModel):
    id: str


@bp.op("/menu_item/delete", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_delete(params: ParamsMenuItemDelete):
    item = g.adal.get_or_404(MenuItem, params.id)
    return {"item": item}


class ParamsMenuItemBulkDelete(APIModel):
    ids: list[str]


@bp.op("/menu_item/bulk_delete", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_bulk_delete(params: ParamsMenuItemBulkDelete):
    items = g.adal.bulk_get(MenuItem, params.ids)
    return {"items": items}
