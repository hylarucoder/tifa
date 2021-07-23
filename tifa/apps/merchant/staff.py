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

from . import bp
from ...globals import AsyncDal, db, Dal
from ...models.system import Staff


class TToken(APIModel):
    id: str
    name: str


@bp.op("/token/create", out=TToken, summary="Token", tags=["账户"])
def token_create():
    ...


@bp.op("/token/refresh", out=TToken, summary="Token", tags=["账户"])
def token_refresh():
    ...


@bp.op("/token/verify", out=TToken, summary="Token", tags=["账户"])
def token_verify():
    ...


@bp.op("/token/deactivate_all", out=TToken, summary="Token-Deactivate-All", tags=["账户"])
def token_deactivate_all():
    ...


class TMe(APIModel):
    id: str
    name: str


@bp.item("/me", out=TMe, summary="我", tags=["账户"])
async def profile():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Staff)
    return {"item": merchant}
