import pathlib

import pathlib2
import pytest
from casbin import Enforcer
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from tifa.globals import db
from tifa.models.sys_account import CasbinAdapter, SysCasbinRule


def get_fixture(path):
    return str(pathlib.Path(pathlib.Path(__file__).parent, "./rbac_model.conf"))


@pytest.fixture(scope="session", autouse=True)
async def setup_db():
    async with db.engine.begin() as conn:
        # await conn.run_sync(db.drop_all)
        await conn.run_sync(db.create_all)
    async with db.async_session() as session:
        session: AsyncSession
        rules = (await session.execute(select(SysCasbinRule).order_by(SysCasbinRule.id))).scalars()
        for rule in rules:
            await session.delete(rule)
        await session.commit()

        session.add(SysCasbinRule(ptype="p", v0="alice", v1="data1", v2="read"))
        session.add(SysCasbinRule(ptype="p", v0="bob", v1="data2", v2="write"))
        session.add(SysCasbinRule(ptype="p", v0="data2_admin", v1="data2", v2="read"))
        session.add(SysCasbinRule(ptype="p", v0="data2_admin", v1="data2", v2="write"))
        session.add(SysCasbinRule(ptype="g", v0="alice", v1="data2_admin"))
        await session.commit()
        yield
        await session.close()


@pytest.fixture(scope="session", autouse=True)
async def enforcer(setup_db):
    adapter = CasbinAdapter()
    return Enforcer(get_fixture("rbac_model.conf"), adapter)


@pytest.mark.asyncio
async def test_enforcer_basic(enforcer):
    assert await enforcer.enforce("alice", "data1", "read")
    # assert False == enforcer.enforce("alice", "data1", "write")
    # assert False == enforcer.enforce("bob", "data1", "read")
    # assert False == enforcer.enforce("bob", "data1", "write")
    # assert enforcer.enforce("bob", "data2", "write")
    # assert False == enforcer.enforce("bob", "data2", "read")
    # assert enforcer.enforce("alice", "data2", "read")
    # assert enforcer.enforce("alice", "data2", "write")

# @pytest.mark.asyncio
# def test_add_policy(enforcer):
#     assert False == enforcer.enforce("eve", "data3", "read")
#     res = enforcer.add_policies((("eve", "data3", "read"), ("eve", "data4", "read")))
#     assert res
#     assert enforcer.enforce("eve", "data3", "read")
#     assert enforcer.enforce("eve", "data4", "read")
#
#
# @pytest.mark.asyncio
# def test_add_policies(enforcer):
#     assert False == enforcer.enforce("eve", "data3", "read")
#     res = enforcer.add_permission_for_user("eve", "data3", "read")
#     assert res
#     assert enforcer.enforce("eve", "data3", "read") @ pytest.mark.asyncio
#
#
# def test_save_policy(enforcer):
#     assert False == enforcer.enforce("alice", "data4", "read")
#
#     model = enforcer.get_model()
#     model.clear_policy()
#
#     model.add_policy("p", "p", ["alice", "data4", "read"])
#
#     adapter = enforcer.get_adapter()
#     adapter.save_policy(model)
#     assert enforcer.enforce("alice", "data4", "read")
#
#
# @pytest.mark.asyncio
# def test_remove_policy(enforcer):
#     assert False == enforcer.enforce("alice", "data5", "read")
#     enforcer.add_permission_for_user("alice", "data5", "read")
#     assert enforcer.enforce("alice", "data5", "read")
#     enforcer.delete_permission_for_user("alice", "data5", "read")
#     assert False == enforcer.enforce("alice", "data5", "read")
#
#
# @pytest.mark.asyncio
# def test_remove_policies(enforcer):
#     assert False == enforcer.enforce("alice", "data5", "read")
#     assert False == enforcer.enforce("alice", "data6", "read")
#     enforcer.add_policies((("alice", "data5", "read"), ("alice", "data6", "read")))
#     assert enforcer.enforce("alice", "data5", "read")
#     assert enforcer.enforce("alice", "data6", "read")
#     enforcer.remove_policies((("alice", "data5", "read"), ("alice", "data6", "read")))
#     assert False == enforcer.enforce("alice", "data5", "read")
#     assert False == enforcer.enforce("alice", "data6", "read")
#
#
# @pytest.mark.asyncio
# def test_remove_filtered_policy(enforcer):
#     assert enforcer.enforce("alice", "data1", "read")
#     enforcer.remove_filtered_policy(1, "data1")
#     assert False == enforcer.enforce("alice", "data1", "read")
#
#     assert enforcer.enforce("bob", "data2", "write")
#     assert enforcer.enforce("alice", "data2", "read")
#     assert enforcer.enforce("alice", "data2", "write")
#
#     enforcer.remove_filtered_policy(1, "data2", "read")
#
#     assert enforcer.enforce("bob", "data2", "write")
#     assert False == enforcer.enforce("alice", "data2", "read")
#     assert enforcer.enforce("alice", "data2", "write")
#
#     enforcer.remove_filtered_policy(2, "write")
#
#     assert False == enforcer.enforce("bob", "data2", "write")
#     assert False == enforcer.enforce("alice", "data2", "write")
#
#     # e.add_permission_for_user('alice', 'data6', 'delete')
#     # e.add_permission_for_user('bob', 'data6', 'delete')
#     # e.add_permission_for_user('eve', 'data6', 'delete')
#     # assert enforcer.enforce('alice', 'data6', 'delete')
#     # assert enforcer.enforce('bob', 'data6', 'delete')
#     # assert enforcer.enforce('eve', 'data6', 'delete')
#     # e.remove_filtered_policy(0, 'alice', None, 'delete')
#     # assert False == enforcer.enforce('alice', 'data6', 'delete')
#     # e.remove_filtered_policy(0, None, None, 'delete')
#     # assert False == enforcer.enforce('bob', 'data6', 'delete')
#     # assert False == enforcer.enforce('eve', 'data6', 'delete')
#
#
# @pytest.mark.asyncio
# def test_str(enforcer):
#     rule = SysCasbinRule(ptype="p", v0="alice", v1="data1", v2="read")
#     assert str(rule) == "p, alice, data1, read"
#     rule = SysCasbinRule(ptype="p", v0="bob", v1="data2", v2="write")
#     assert str(rule) == "p, bob, data2, write"
#     rule = SysCasbinRule(ptype="p", v0="data2_admin", v1="data2", v2="read")
#     assert str(rule) == "p, data2_admin, data2, read"
#     rule = SysCasbinRule(ptype="p", v0="data2_admin", v1="data2", v2="write")
#     assert str(rule) == "p, data2_admin, data2, write"
#     rule = SysCasbinRule(ptype="g", v0="alice", v1="data2_admin")
#     assert str(rule) == "g, alice, data2_admin"
#
#
# @pytest.mark.asyncio
# def test_repr(enforcer):
#     rule = SysCasbinRule(ptype="p", v0="alice", v1="data1", v2="read")
#     assert (repr(rule), '<CasbinRule None: "p, alice, data1, read">')
#     Base.metadata.create_all(engine)
#     s = session()
#
#     s.add(rule)
#     s.commit()
#     self.assertRegex(repr(rule), r'<CasbinRule \d+: "p, alice, data1, read">')
#     s.close()
#
#
# @pytest.mark.asyncio
# def test_filtered_policy(enforcer):
#     filter = Filter()
#
#     filter.ptype = ["p"]
#     enforcer.load_filtered_policy(filter)
#     assert enforcer.enforce("alice", "data1", "read")
#     assert False == enforcer.enforce("alice", "data1", "write")
#     assert False == enforcer.enforce("alice", "data2", "read")
#     assert False == enforcer.enforce("alice", "data2", "write")
#     assert False == enforcer.enforce("bob", "data1", "read")
#     assert False == enforcer.enforce("bob", "data1", "write")
#     assert False == enforcer.enforce("bob", "data2", "read")
#     assert enforcer.enforce("bob", "data2", "write")
#
#     filter.ptype = []
#     filter.v0 = ["alice"]
#     enforcer.load_filtered_policy(filter)
#     assert enforcer.enforce("alice", "data1", "read")
#     assert False == enforcer.enforce("alice", "data1", "write")
#     assert False == enforcer.enforce("alice", "data2", "read")
#     assert False == enforcer.enforce("alice", "data2", "write")
#     assert False == enforcer.enforce("bob", "data1", "read")
#     assert False == enforcer.enforce("bob", "data1", "write")
#     assert False == enforcer.enforce("bob", "data2", "read")
#     assert False == enforcer.enforce("bob", "data2", "write")
#     assert False == enforcer.enforce("data2_admin", "data2", "read")
#     assert False == enforcer.enforce("data2_admin", "data2", "write")
#
#     filter.v0 = ["bob"]
#     enforcer.load_filtered_policy(filter)
#     assert False == enforcer.enforce("alice", "data1", "read")
#     assert False == enforcer.enforce("alice", "data1", "write")
#     assert False == enforcer.enforce("alice", "data2", "read")
#     assert False == enforcer.enforce("alice", "data2", "write")
#     assert False == enforcer.enforce("bob", "data1", "read")
#     assert False == enforcer.enforce("bob", "data1", "write")
#     assert False == enforcer.enforce("bob", "data2", "read")
#     assert enforcer.enforce("bob", "data2", "write")
#     assert False == enforcer.enforce("data2_admin", "data2", "read")
#     assert False == enforcer.enforce("data2_admin", "data2", "write")
#
#     filter.v0 = ["data2_admin"]
#     enforcer.load_filtered_policy(filter)
#     assert enforcer.enforce("data2_admin", "data2", "read")
#     assert enforcer.enforce("data2_admin", "data2", "read")
#     assert False == enforcer.enforce("alice", "data1", "read")
#     assert False == enforcer.enforce("alice", "data1", "write")
#     assert False == enforcer.enforce("alice", "data2", "read")
#     assert False == enforcer.enforce("alice", "data2", "write")
#     assert False == enforcer.enforce("bob", "data1", "read")
#     assert False == enforcer.enforce("bob", "data1", "write")
#     assert False == enforcer.enforce("bob", "data2", "read")
#     assert False == enforcer.enforce("bob", "data2", "write")
#
#     filter.v0 = ["alice", "bob"]
#     enforcer.load_filtered_policy(filter)
#     assert enforcer.enforce("alice", "data1", "read")
#     assert False == enforcer.enforce("alice", "data1", "write")
#     assert False == enforcer.enforce("alice", "data2", "read")
#     assert False == enforcer.enforce("alice", "data2", "write")
#     assert False == enforcer.enforce("bob", "data1", "read")
#     assert False == enforcer.enforce("bob", "data1", "write")
#     assert False == enforcer.enforce("bob", "data2", "read")
#     assert enforcer.enforce("bob", "data2", "write")
#     assert False == enforcer.enforce("data2_admin", "data2", "read")
#     assert False == enforcer.enforce("data2_admin", "data2", "write")
#
#     filter.v0 = []
#     filter.v1 = ["data1"]
#     enforcer.load_filtered_policy(filter)
#     assert enforcer.enforce("alice", "data1", "read")
#     assert False == enforcer.enforce("alice", "data1", "write")
#     assert False == enforcer.enforce("alice", "data2", "read")
#     assert False == enforcer.enforce("alice", "data2", "write")
#     assert False == enforcer.enforce("bob", "data1", "read")
#     assert False == enforcer.enforce("bob", "data1", "write")
#     assert False == enforcer.enforce("bob", "data2", "read")
#     assert False == enforcer.enforce("bob", "data2", "write")
#     assert False == enforcer.enforce("data2_admin", "data2", "read")
#     assert False == enforcer.enforce("data2_admin", "data2", "write")
#
#     filter.v1 = ["data2"]
#     enforcer.load_filtered_policy(filter)
#     assert False == enforcer.enforce("alice", "data1", "read")
#     assert False == enforcer.enforce("alice", "data1", "write")
#     assert False == enforcer.enforce("alice", "data2", "read")
#     assert False == enforcer.enforce("alice", "data2", "write")
#     assert False == enforcer.enforce("bob", "data1", "read")
#     assert False == enforcer.enforce("bob", "data1", "write")
#     assert False == enforcer.enforce("bob", "data2", "read")
#     assert enforcer.enforce("bob", "data2", "write")
#     assert enforcer.enforce("data2_admin", "data2", "read")
#     assert enforcer.enforce("data2_admin", "data2", "write")
#
#     filter.v1 = []
#     filter.v2 = ["read"]
#     enforcer.load_filtered_policy(filter)
#     assert enforcer.enforce("alice", "data1", "read")
#     assert False == enforcer.enforce("alice", "data1", "write")
#     assert False == enforcer.enforce("alice", "data2", "read")
#     assert False == enforcer.enforce("alice", "data2", "write")
#     assert False == enforcer.enforce("bob", "data1", "read")
#     assert False == enforcer.enforce("bob", "data1", "write")
#     assert False == enforcer.enforce("bob", "data2", "read")
#     assert False == enforcer.enforce("bob", "data2", "write")
#     assert enforcer.enforce("data2_admin", "data2", "read")
#     assert False == enforcer.enforce("data2_admin", "data2", "write")
#
#     filter.v2 = ["write"]
#     enforcer.load_filtered_policy(filter)
#     assert False == enforcer.enforce("alice", "data1", "read")
#     assert False == enforcer.enforce("alice", "data1", "write")
#     assert False == enforcer.enforce("alice", "data2", "read")
#     assert False == enforcer.enforce("alice", "data2", "write")
#     assert False == enforcer.enforce("bob", "data1", "read")
#     assert False == enforcer.enforce("bob", "data1", "write")
#     assert False == enforcer.enforce("bob", "data2", "read")
#     assert enforcer.enforce("bob", "data2", "write")
#     assert False == enforcer.enforce("data2_admin", "data2", "read")
#     assert enforcer.enforce("data2_admin", "data2", "write")
