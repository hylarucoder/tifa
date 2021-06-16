from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, DeclarativeMeta

from tifa.settings import get_settings


class SQLAlchemy:
    async_session: AsyncSession

    # Model: Base

    def __init__(self):
        self.Model = declarative_base()
        self.engine = self.create_engine()
        self.async_session: AsyncSession = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    def create_engine(self):
        return create_async_engine(get_settings().POSTGRES_DATABASE_URI, echo=True)

    def create_all(self, connection):
        return self.Model.metadata.create_all(bind=connection)

    def drop_all(self, connection):
        return self.Model.metadata.drop_all(bind=connection)
