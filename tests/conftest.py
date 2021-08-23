import asyncio

import pytest
from requests import Response
from starlette.testclient import TestClient

from tifa.app import create_app
from tifa.auth import gen_jwt
from tifa.db.adal import AsyncDal
from tifa.globals import db
from tifa.models.product import ProductType
from tifa.models.system import Staff
from tifa.models.user import User


class ApiClient(TestClient):
    def __init__(self, app, prefix="", user=None, *args, **kwargs):
        self.user = user
        self.prefix = prefix
        super().__init__(app, *args, **kwargs)

    def get(self, url: str, **kwargs) -> Response:
        return super().get(url, **kwargs)

    def op(self, url: str, json=None, **kwargs) -> Response:
        res = super().post(url, None, json, **kwargs).json()
        if "item" in res:
            return res["item"]
        return res


app = create_app()


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    with db.engine.begin() as conn:
        db.drop_all(conn)
        db.create_all(conn)
    yield
    conn.close()


@pytest.fixture(scope="session")
async def adal(event_loop, setup_db) -> AsyncDal:
    adal = AsyncDal(db.async_session)
    yield adal
    await adal.session.close()


@pytest.fixture(scope="session")
async def staff(adal):
    ins = adal.add(
        Staff,
        name="admin",
    )
    await adal.commit()
    return ins


@pytest.fixture(scope="session")
async def user():
    ins = adal.add(
        User,
        name="alphago",
    )
    await adal.commit()
    return ins


@pytest.fixture(scope="session")
def staff_client(staff):
    client = ApiClient(app, staff)
    token = gen_jwt("{\"admin\":1}", 60 * 24)
    client.headers.update({
        "Authorization": f"Bearer {token}"
    })
    return client


@pytest.fixture(scope="session")
def user_client(user):
    return ApiClient(app, user)


@pytest.fixture(scope="session")
def health_client():
    return ApiClient(app)


@pytest.fixture
async def product_type(color_attribute, size_attribute):
    product_type = ProductType.objects.create(
        name="Default Type",
        slug="default-type",
        has_variants=True,
        is_shipping_required=True,
    )
    product_type.product_attributes.add(color_attribute)
    product_type.variant_attributes.add(size_attribute)
    return product_type
