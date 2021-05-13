from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from tifa.settings import get_settings

print(get_settings().POSTGRES_DATABASE_URI)


class SQLAlchemy:
    def __init__(self):
        self.Model = declarative_base()
        self.engine = self.create_engine()
        self.session: AsyncSession = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    def create_engine(self):
        return create_async_engine(get_settings().POSTGRES_DATABASE_URI, echo=True)

    def create_all(self, connection):
        return self.Model.metadata.create_all(bind=connection)

    def drop_all(self, connection):
        return self.Model.metadata.drop_all(bind=connection)
