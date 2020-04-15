from functools import lru_cache
from typing import List

from pydantic import BaseSettings


class TifaSettings(BaseSettings):
    api_v1_route: str = "/api/v1"
    openapi_route: str = "/api/v1/openapi.json"

    settings: str = ""
    static_mount_path: str = ""
    static_dir: str = ""

    debug: bool = False

    class Config:
        env_prefix = ""


@lru_cache()
def get_settings() -> TifaSettings:
    return TifaSettings()  # reads variables from environment
