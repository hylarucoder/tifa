from fastapi_utils.api_model import APIModel

from tifa.apps.merchant import bp
from tifa.models.warehouse import Warehouse


class TWarehouse(APIModel):
    id: str
    name: str


@bp.list(
    "/ware_houses",
    out=TWarehouse,
    summary="WareHouse",
    tags=["WareHouse"],
)
def webhook_list():
    return []


@bp.item(
    "/ware_house",
    out=TWarehouse,
    summary="WareHouse",
    tags=["WareHouse"],
)
def webhook_item():
    Warehouse
    return []
