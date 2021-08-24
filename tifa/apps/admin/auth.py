from fastapi_utils.api_model import APIModel
from opentelemetry import trace

from tifa.apps.admin import bp
from tifa.apps.admin.local import g
from tifa.auth import verify_password, gen_jwt
from tifa.exceptions import ApiException
from tifa.models.system import Staff

tracer = trace.get_tracer(__name__)


class TMe(APIModel):
    id: str
    name: str


@bp.item("/me", out=TMe, summary="我", tags=["Auth"])
async def profile():
    staff = g.staff
    return {"item": staff}


class TLogin(APIModel):
    id: str
    name: str
    token: str


class BLogin(APIModel):
    name: str
    password: str


@bp.op("/login", out=TLogin, summary="登陆", tags=["Auth"])
async def login(b: BLogin):
    with tracer.start_as_current_span("foo"):
        with tracer.start_as_current_span("bar"):
            with tracer.start_as_current_span("baz"):
                print("Hello world from OpenTelemetry Python!")

    adal = g.adal
    staff = await adal.first_or_404(Staff, Staff.name == b.name)
    if not verify_password(b.password, staff.password_hash):
        raise ApiException("not valid")
    return {
        "item": {
            "id": staff.id,
            "name": staff.name,
            "token": gen_jwt('{"admin":1}', 60 * 24),
        }
    }
