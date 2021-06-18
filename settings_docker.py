from tifa.settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DATABASE_URI: str = "postgresql+asyncpg://tifa:tifa123@postgres:5432/tifa"
