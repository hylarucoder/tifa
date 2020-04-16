from functools import lru_cache
from pydantic import BaseSettings, PostgresDsn


class TifaSettings(BaseSettings):
    TITLE: str = "Tifa Lockhart"
    DESCRIPTION: str = "Yet another opinionated fastapi-start-kit with best practice"
    API_V1_ROUTE: str = "/api/v1"
    OPED_API_ROUTE: str = "/api/v1/openapi.json"

    STATIC_PATH: str = "/static"
    STATIC_DIR: str = "static"

    DEBUG: bool = False
    ENV: str = "LOCAL"

    POSTGRES_DATABASE_URI: PostgresDsn = 'postgresql://tifa:tifa@localhost:5432/tifa'

    class Config:
        case_sensitive = True
        env_prefix = "TIFA_"


@lru_cache()
def get_settings() -> TifaSettings:
    # override if required
    return TifaSettings(_env_file=".env")
