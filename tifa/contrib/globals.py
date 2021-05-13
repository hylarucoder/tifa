# thanks to https://gist.github.com/ddanier/ead419826ac6c3d75c96f9d89bea9bd0
from contextvars import ContextVar
from typing import Any

from starlette.types import ASGIApp, Scope, Receive, Send


class Globals:
    __slots__ = ("_vars",)

    _vars: dict[str, ContextVar]

    def __init__(self) -> None:
        object.__setattr__(self, "_vars", {})

    def reset(self) -> None:
        for _name, var in self._vars.items():
            var.set(None)

    def _ensure_var(self, item: str) -> None:
        if item not in self._vars:
            self._vars[item] = ContextVar(f"globals:{item}")
            self._vars[item].set(None)

    def __getattr__(self, item: str) -> Any:
        self._ensure_var(item)
        try:
            return self._vars[item].get()
        except LookupError:
            self._vars[item].set(None)
            return None

    def __setattr__(self, item: str, value: Any) -> None:
        self._ensure_var(item)
        self._vars[item].set(value)


class GlobalsMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        glb.reset()
        await self.app(scope, receive, send)


glb = Globals()
