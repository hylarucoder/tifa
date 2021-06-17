import asyncio

import pytest

from tifa.app import create_app
from tifa.globals import db
from tifa.models.sys_account import SysUser
from tifa.settings import get_settings

current_app = create_app(settings=get_settings(env="test"))


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def setup_db():
    async with db.engine.begin() as conn:
        await conn.run_sync(db.drop_all)
        await conn.run_sync(db.create_all)

    await SysUser.add(
        name="name",
    )
    await db.session.commit()
    yield
    await conn.close()
