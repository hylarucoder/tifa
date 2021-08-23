"""
addressSetDefault(...): AddressSetDefault

accountAddressCreate(...): AccountAddressCreate
accountAddressDelete(...): AccountAddressDelete
accountAddressUpdate(...): AccountAddressUpdate
"""
from fastapi_utils.api_model import APIModel

from tifa.apps.admin.local import g
from tifa.apps.admin.router import bp
from tifa.models.address import Address


class TAddress(APIModel):
    id: str
    name: str


@bp.list("/addresses", out=TAddress, summary="Address", tags=["Address"])
def addresses_list():
    ins = g.adal.first_or_404(Address)
    return {"items": ins}


@bp.item("/address", out=TAddress, summary="Address", tags=["Address"])
def address_item():
    ins = g.adal.first_or_404(Address)
    return {"items": ins}


@bp.op("/address/create", out=TAddress, summary="Address", tags=["Address"])
def address_create():
    ins = g.adal.first_or_404(Address)
    return {"items": ins}


@bp.op("/address/update", out=TAddress, summary="Address", tags=["Address"])
def address_update():
    ins = g.adal.first_or_404(Address)
    return {"items": ins}


@bp.op("/address/set_default", out=TAddress, summary="Address", tags=["Address"])
def address_set_default():
    ins = g.adal.first_or_404(Address)
    return {"items": ins}


@bp.op("/address/delete", out=TAddress, summary="Address", tags=["Address"])
def address_delete():
    ins = g.adal.first_or_404(Address)
    return {"items": ins}


@bp.op("/address/validation_rules", out=TAddress, summary="Address", tags=["Address"])
def address_validation_rule():
    ins = g.adal.first_or_404(Address)
    return {"items": ins}
