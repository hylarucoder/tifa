import typing as t

from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from tifa.db.pagination import Pagination
from tifa.exceptions import NotFound

T = t.TypeVar("T")


class AsyncDal:
    """
    通用方法
    - 获取 id 用 get
    """

    session: AsyncSession

    def __init__(self, s):
        self.session = s

    async def get(self, clz: T, id: str) -> t.Optional[T]:
        return await self.session.get(clz, int(id))

    async def bulk_get(self, clz: T, ids: list[str]) -> list[T]:
        return (
            (await self.session.execute(sa.select(clz).where(clz.id.in_(ids))))
            .scalars()
            .all()
        )

    async def get_or_404(self, clz: T, id) -> T:
        ins = await self.session.get(clz, int(id))
        if not ins:
            raise NotFound(f"{clz} not found")
        return ins

    async def first_or_404(self, clz: T, *args) -> T:
        ins = (
            (await self.session.execute(sa.select(clz).where(*args))).scalars().first()
        )
        if not ins:
            raise NotFound(f"{clz} not found")
        return ins

    async def first(self, stmt: T) -> T:
        return (await self.session.execute(stmt)).scalars().first()

    async def last(self, stmt: T) -> T:
        return (await self.session.execute(stmt)).scalars().first()

    async def all(self, clz: T, *args) -> list[T]:
        return (await self.session.execute(sa.select(clz).where(*args))).scalars().all()

    async def unique_all(self, stmt: T) -> list[T]:
        return (await self.session.execute(stmt)).unique().scalars().all()

    async def page(self, cls: T, per_page=20, page=1) -> Pagination:
        stmt = sa.select(cls)
        stmt_items = stmt.limit(per_page).offset((page - 1) * per_page)
        total = (
            (
                await self.session.execute(
                    sa.select(sa.func.count()).select_from(stmt.subquery())
                )
            )
            .scalars()
            .one()
        )
        items = (await self.session.execute(stmt_items)).scalars().all()
        return Pagination(page, per_page, total, items)

    def add(self, clz: T, **kwargs) -> T:
        obj = clz(**kwargs)
        self.session.add(obj)
        return obj

    def delete(self, ins: T) -> T:
        self.session.delete(ins)
        return self

    async def commit(self):
        await self.session.commit()
