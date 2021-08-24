import asyncio
import datetime

import pytest
from requests import Response
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.testclient import TestClient

from tifa.app import create_app
from tifa.auth import gen_jwt
from tifa.db.adal import AsyncDal
from tifa.globals import db
from tifa.models.attr import Attribute, AttributeValue
from tifa.models.product import ProductType
from tifa.models.product_attr import AttributeProduct
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
async def session(setup_db) -> AsyncSession:
    async with db.AsyncSession() as session:
        yield session


@pytest.fixture(scope="session")
async def staff(session: AsyncSession):
    adal = AsyncDal(session)
    ins = adal.add(
        Staff,
        name="admin",
    )
    await adal.commit()
    return ins


@pytest.fixture(scope="session")
async def user(session: AsyncSession):
    adal = AsyncDal(session)
    ins = adal.add(
        User,
        email="alphago@gmail.com",
        is_active=True,
        password="plain_password",
        last_login_at=datetime.datetime.now(),
        first_name="alpha",
        last_name="go",
    )
    await adal.commit()
    return ins


@pytest.fixture(scope="session")
def staff_client(staff: Staff):
    client = ApiClient(app, staff)
    token = gen_jwt("{\"admin\":1}", 60 * 24)
    client.headers.update({
        "Authorization": f"Bearer {token}"
    })
    return client


@pytest.fixture(scope="session")
def user_client(user: User):
    return ApiClient(app, user)


@pytest.fixture(scope="session")
def health_client():
    return ApiClient(app)


@pytest.fixture(scope="session")
async def color_attribute(session: AsyncSession):
    adal = AsyncDal(session)
    attribute = adal.add(
        Attribute,
        slug="color",
        name="Color",
        type=Attribute.Type.PRODUCT,
        input_type=Attribute.InputType.DROPDOWN,
        filterable_in_storefront=True,
        filterable_in_dashboard=True,
        available_in_grid=True,
    )
    adal.add(AttributeValue, attribute=attribute, name="Red", slug="red", value="red")
    adal.add(AttributeValue, attribute=attribute, name="Blue", slug="blue", value="blue")
    await adal.commit()
    return attribute


@pytest.fixture(scope="session")
async def size_attribute(session: AsyncSession):
    adal = AsyncDal(session)
    attribute = adal.add(
        Attribute,
        slug="size",
        name="Size",
        type=Attribute.Type.PRODUCT,
        input_type=Attribute.InputType.DROPDOWN,
        filterable_in_storefront=True,
        filterable_in_dashboard=True,
        available_in_grid=True,
    )
    adal.add(AttributeValue, attribute=attribute, name="3XL", slug="3xl", value="3xl")
    adal.add(AttributeValue, attribute=attribute, name="2XL", slug="2xl", value="2xl")
    adal.add(AttributeValue, attribute=attribute, name="XL", slug="xl", value="xl")
    adal.add(AttributeValue, attribute=attribute, name="L", slug="l", value="l")
    await adal.commit()
    return attribute


@pytest.fixture(scope="session")
async def date_attribute(session: AsyncSession):
    adal = AsyncDal(session)
    attribute = adal.add(
        Attribute,
        slug="release-date",
        name="Release date",
        type=Attribute.Type.PRODUCT,
        input_type=Attribute.InputType.DATE,
        filterable_in_storefront=True,
        filterable_in_dashboard=True,
        available_in_grid=True,
    )
    for value in [
        datetime.datetime(2020, 10, 5),
        datetime.datetime(2020, 11, 5),
    ]:
        adal.add(
            AttributeValue,
            attribute=attribute,
            name=f"{attribute.name}: {value.date()}",
            slug=f"{value.date()}_{attribute.id}",
            value=f"{value.date()}",
        )
    await adal.commit()

    return attribute


@pytest.fixture(scope="session")
async def date_time_attribute(session: AsyncSession):
    adal = AsyncDal(session)
    attribute = adal.add(
        Attribute,
        slug="release-date-time",
        name="Release date time",
        type=Attribute.Type.PRODUCT,
        input_type=Attribute.InputType.DATE_TIME,
        filterable_in_storefront=True,
        filterable_in_dashboard=True,
        available_in_grid=True,
    )

    for value in [
        datetime.datetime(2020, 10, 5),
        datetime.datetime(2020, 11, 5),
    ]:
        adal.add(
            AttributeValue,
            attribute=attribute,
            name=f"{attribute.name}: {value.date()}",
            slug=f"{value.date()}_{attribute.id}",
            value=f"{value.date()}",
        )
    await adal.commit()

    return attribute


@pytest.fixture(scope="session")
async def product_type(session: AsyncSession, color_attribute, size_attribute):
    adal = AsyncDal(session)
    product_type = adal.add(
        ProductType,
        name="Default Type",
        slug="default-type",
        has_variants=True,
        is_shipping_required=True,
        weight=0.1,
        is_digital=True,
    )
    adal.add(
        AttributeProduct,
        attribute=color_attribute,
        product_type=product_type,
    )
    adal.add(
        AttributeProduct,
        attribute=size_attribute,
        product_type=product_type,
    )
    await adal.commit()
    return product_type
