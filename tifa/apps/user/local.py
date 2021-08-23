from contextvars import ContextVar

from tifa.db.adal import AsyncDal
from tifa.models.user import User

context_default = {
    "user": None,
    "adal": None,
}
_context = ContextVar("_context", default=context_default.copy())


class Context:
    _context: ContextVar

    def __init__(self):
        self._context = _context

    @property
    def adal(self):
        return self._context.get()["adal"]

    @adal.setter
    def adal(self, v: AsyncDal):
        self._context.get()["adal"] = v

    @property
    def staff(self):
        return self._context.get()["user"]

    @staff.setter
    def staff(self, v: User):
        self._context.get()["user"] = v


g = Context()
