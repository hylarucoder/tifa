import json

from fastapi import FastAPI
from fastapi.responses import Response

from tifa.settings import BasicSettings, get_settings


class ApiResult:
    def __init__(self, value, status_code=200, next_page=None):
        self.value = value
        self.status_code = status_code
        self.nex_page = next_page

    def to_response(self):
        return Response(
            json.dumps(self.value, ensure_ascii=False),  # TODO: polish
            status_code=self.status_code,
            # mimetype="application/json",
        )


class TifaFastApi(FastAPI):
    @property
    def settings(self) -> BasicSettings:
        return get_settings()
