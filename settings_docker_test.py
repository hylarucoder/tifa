from tifa.conf import GlobalSetting


class Setting(GlobalSetting):
    ENV = "TEST"
    POSTGRES_DATABASE_URI: str = "postgresql://tifa:tifa123@postgres:5432/tifa_test"
    POSTGRES_DATABASE_URI_ASYNC: str = "postgresql+asyncpg://tifa:tifa123@postgres:5432/tifa_test"
