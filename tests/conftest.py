import asyncio

import pytest

from tifa.app import create_app
from tifa.globals import db
from tifa.models.sys_account import SysUser

current_app = create_app()


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

    SysUser.add(
        name="name",
    )
    db.session.commit()
    yield
    conn.close()
