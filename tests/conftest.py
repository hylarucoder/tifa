import asyncio

import pytest
from requests import Response
from starlette.testclient import TestClient

from tifa.app import create_app
from tifa.globals import db, Dal
from tifa.models.system import Staff
from tifa.models.user import User


class ApiClient(TestClient):
    def __init__(self, app, user=None, *args, **kwargs):
        self.user = user
        super().__init__(app, *args, **kwargs)

    def get(self, url: str, **kwargs) -> Response:
        return super().get(url, **kwargs)

    def post(self, url: str, data=None, json=None, **kwargs) -> Response:
        return super().post(url, data, json, **kwargs)


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
def staff():
    dal = Dal(db.session)
    ins = dal.add(
        Staff,
        name="admin",
    )
    dal.commit()
    return ins


@pytest.fixture(scope="session")
def user():
    dal = Dal(db.session)
    ins = dal.add(
        User,
        name="name",
    )
    dal.commit()
    return ins


@pytest.fixture
def staff_client(staff):
    return ApiClient(app, staff)


@pytest.fixture
def user_client(user):
    return ApiClient(app, user)


@pytest.fixture
def health_client():
    return ApiClient(app)
