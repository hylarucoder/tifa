import typing as t
from typing import Union

import sqlalchemy as sa
from sqlalchemy.orm import Session

from tifa.db.pagination import Pagination
from tifa.exceptions import NotFound
from tifa.globals import session

T = t.TypeVar("T")


class Dal:
    """
    通用方法
    - 获取 id 用 get
    """

    session: Session

    def __init__(self, s=None):
        if not s:
            self.session = session
        else:
            self.session = s

    def get(self, clz: T, id: str) -> t.Optional[T]:
        return self.session.get(clz, id)

    def bulk_get(self, clz: T, ids: list[str]) -> list[T]:
        return (
            self.session.execute(sa.select(clz).where(clz.id.in_(ids))).scalars().all()
        )

    def get_or_404(self, clz: T, id) -> T:
        ins = self.session.get(clz, id)
        if not ins:
            raise NotFound("not found")
        return ins

    def first_or_404(self, clz: T, stmt_func: t.Callable[[sa.select], sa.select]) -> T:
        stmt = stmt_func(sa.select(clz))
        ins = self.session.execute(stmt).scalars().first()
        if not ins:
            raise NotFound("not found")
        return ins

    def first(
        self, clz: T, stmt_func: t.Callable[[sa.select], sa.select] = lambda x: x
    ) -> T:
        stmt = stmt_func(sa.select(clz))
        return self.session.execute(stmt).scalars().first()

    def last(
        self, clz: T, stmt_func: t.Callable[[sa.select], sa.select] = lambda x: x
    ) -> T:
        stmt = stmt_func(sa.select(clz))
        return self.session.execute(stmt).scalars().first()

    def all(
        self, clz: T, stmt_func: t.Callable[[sa.select], sa.select] = lambda x: x
    ) -> list[T]:
        stmt = stmt_func(sa.select(clz))
        return self.session.execute(stmt).scalars().all()

    def unique_all(
        self, clz: T, stmt_func: t.Callable[[sa.select], sa.select] = lambda x: x
    ) -> list[T]:
        stmt = stmt_func(sa.select(clz))
        return self.session.execute(stmt).unique().scalars().all()

    def page(
        self,
        clz: T,
        stmt_func: t.Callable[[sa.select], sa.select] = lambda x: x,
        per_page=20,
        page=1,
    ) -> Pagination:
        stmt = stmt_func(sa.select(clz))
        stmt_items = stmt.limit(per_page).offset((page - 1) * per_page)
        total = (
            self.session.execute(
                sa.select(sa.func.count()).select_from(stmt.subquery())
            )
            .scalars()
            .one()
        )
        items = self.session.execute(stmt_items).scalars().all()
        return Pagination(page, per_page, total, items)

    def add(self, clz: T, **kwargs) -> T:
        obj = clz(**kwargs)
        self.session.add(obj)
        return obj

    def delete(self, ins: T):
        self.session.delete(ins)

    def commit(self):
        self.session.commit()
