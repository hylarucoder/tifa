"""

accountDelete(...): AccountDelete
accountRegister(...): AccountRegister
accountRequestDeletion(...): AccountRequestDeletion
accountSetDefaultAddress(...): AccountSetDefaultAddress
accountUpdate(...): AccountUpdate

staffCreate(...): StaffCreate
staffDelete(...): StaffDelete
staffBulkDelete(...): StaffBulkDelete
staffUpdate(...): StaffUpdate
staffUsers(...): UserCountableConnection

staffNotificationRecipientCreate(...): StaffNotificationRecipientCreate
staffNotificationRecipientDelete(...): StaffNotificationRecipientDelete
staffNotificationRecipientUpdate(...): StaffNotificationRecipientUpdate
"""

from fastapi_utils.api_model import APIModel

from tifa.apps.admin import bp
from tifa.auth import get_password_hash
from tifa.db.adal import AsyncDal
from tifa.globals import db
from tifa.models.system import Staff
from tifa.apps.admin.local import g


class TToken(APIModel):
    id: str
    name: str


@bp.op("/token/create", out=TToken, summary="Token", tags=["Profile"])
def token_create():
    ...


@bp.op("/token/refresh", out=TToken, summary="Token", tags=["Profile"])
def token_refresh():
    ...


@bp.op("/token/verify", out=TToken, summary="Token", tags=["Profile"])
def token_verify():
    ...


@bp.op(
    "/token/deactivate_all",
    out=TToken,
    summary="Token-Deactivate-All",
    tags=["Profile"],
)
def token_deactivate_all():
    ...


class TStaff(APIModel):
    id: str
    name: str
    is_admin: bool


@bp.page("/staffs", out=TStaff, summary="Staff", tags=["Staff"])
async def get_staffs():
    adal = AsyncDal(db.async_session)
    ...


@bp.item("/staff/{id}", out=TStaff, summary="Staff", tags=["Staff"])
async def get_staffs(id: str):
    ...


class BStaffCreate(APIModel):
    name: str
    password: str


@bp.op("/staff/create", out=TStaff, summary="Staff", tags=["Staff"])
async def staff_create(b: BStaffCreate):
    g.adal.add(
        Staff,
        name=b.name,
        password_hash=get_password_hash(b.password),
    )
    g.adal.commit()


@bp.op("/staff/update", out=TStaff, summary="Staff", tags=["Staff"])
async def staff_update():
    ...


@bp.op("/staff/delete", out=TStaff, summary="Staff", tags=["Staff"])
async def staff_delete():
    ...
