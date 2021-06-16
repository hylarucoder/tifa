from contextlib import contextmanager

import sqlalchemy as sa
from casbin import persist
from sqlalchemy import or_

from tifa.globals import db
from tifa.models.base import ModelMixin


class SysUser(ModelMixin, db.Model):
    __tablename__ = "sys_user"
    # TODO: need polish
    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}

    id = sa.Column(sa.Integer, primary_key=True)
    nickname = sa.Column(sa.String(50))


class SysCasbinRule(ModelMixin, db.Model):
    __tablename__ = "sys_casbin_rule"

    id = sa.Column(sa.BigInteger, primary_key=True)
    ptype = sa.Column(sa.String(255))
    v0 = sa.Column(sa.String(255))
    v1 = sa.Column(sa.String(255))
    v2 = sa.Column(sa.String(255))
    v3 = sa.Column(sa.String(255))
    v4 = sa.Column(sa.String(255))
    v5 = sa.Column(sa.String(255))

    def __str__(self):
        arr = [self.ptype]
        for v in (self.v0, self.v1, self.v2, self.v3, self.v4, self.v5):
            if v is None:
                break
            arr.append(v)
        return ", ".join(arr)

    def __repr__(self):
        return '<SysCasbinRule {}: "{}">'.format(self.id, str(self))


class CasbinAdapter(persist.Adapter):
    """the interface for Casbin adapters."""

    def __init__(self, filtered=False):
        self._db_class = SysCasbinRule
        self._filtered = filtered

    async def load_policy(self, model):
        """loads all policy rules from the storage."""
        async with db.async_session() as session:
            lines = session.query(self._db_class).all()
            for line in lines:
                persist.load_policy_line(str(line), model)

    def is_filtered(self):
        return self._filtered

    async def load_filtered_policy(self, model, filter) -> None:
        """loads all policy rules from the storage."""
        async with db.async_session() as session:
            query = session.query(self._db_class)
            filters = self.filter_query(query, filter)
            filters = filters.all()

            for line in filters:
                persist.load_policy_line(str(line), model)
            self._filtered = True

    def filter_query(self, query, filter):
        if len(filter.ptype) > 0:
            query = query.filter(SysCasbinRule.ptype.in_(filter.ptype))
        if len(filter.v0) > 0:
            query = query.filter(SysCasbinRule.v0.in_(filter.v0))
        if len(filter.v1) > 0:
            query = query.filter(SysCasbinRule.v1.in_(filter.v1))
        if len(filter.v2) > 0:
            query = query.filter(SysCasbinRule.v2.in_(filter.v2))
        if len(filter.v3) > 0:
            query = query.filter(SysCasbinRule.v3.in_(filter.v3))
        if len(filter.v4) > 0:
            query = query.filter(SysCasbinRule.v4.in_(filter.v4))
        if len(filter.v5) > 0:
            query = query.filter(SysCasbinRule.v5.in_(filter.v5))
        return query.order_by(SysCasbinRule.id)

    async def _save_policy_line(self, ptype, rule):
        async with db.async_session() as session:
            line = self._db_class(ptype=ptype)
            for i, v in enumerate(rule):
                setattr(line, "v{}".format(i), v)
            session.add(line)

    async def save_policy(self, model):
        """saves all policy rules to the storage."""
        async with db.async_session() as session:
            query = session.query(self._db_class)
            query.delete()
            for sec in ["p", "g"]:
                if sec not in model.model.keys():
                    continue
                for ptype, ast in model.model[sec].items():
                    for rule in ast.policy:
                        await self._save_policy_line(ptype, rule)
        return True

    async def add_policy(self, sec, ptype, rule):
        """adds a policy rule to the storage."""
        await self._save_policy_line(ptype, rule)

    async def add_policies(self, sec, ptype, rules):
        """adds a policy rules to the storage."""
        for rule in rules:
            await self._save_policy_line(ptype, rule)

    async def remove_policy(self, sec, ptype, rule):
        """removes a policy rule from the storage."""
        with db.async_session() as session:
            query = session.query(self._db_class)
            query = query.filter(self._db_class.ptype == ptype)
            for i, v in enumerate(rule):
                query = query.filter(getattr(self._db_class, "v{}".format(i)) == v)
            r = query.delete()

        return True if r > 0 else False

    async def remove_policies(self, sec, ptype, rules):
        """removes a policy rules from the storage."""
        if not rules:
            return
        async with db.async_session() as session:
            query = session.query(self._db_class)
            query = query.filter(self._db_class.ptype == ptype)
            rules = zip(*rules)
            for i, rule in enumerate(rules):
                query = query.filter(
                    or_(getattr(self._db_class, "v{}".format(i)) == v for v in rule)
                )
            query.delete()

    async def remove_filtered_policy(self, sec, ptype, field_index, *field_values):
        """removes policy rules that match the filter from the storage.
        This is part of the Auto-Save feature.
        """
        async with db.async_session() as session:
            query = session.query(self._db_class)
            query = query.filter(self._db_class.ptype == ptype)
            if not (0 <= field_index <= 5):
                return False
            if not (1 <= field_index + len(field_values) <= 6):
                return False
            for i, v in enumerate(field_values):
                if v != "":
                    query = query.filter(
                        getattr(self._db_class, "v{}".format(field_index + i)) == v
                    )
            r = query.delete()

        return True if r > 0 else False
