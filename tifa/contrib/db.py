from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from tifa.contrib.globals import glb
from tifa.settings import settings


class SQLAlchemy:
    # Model: t.Type[BaseModel]
    Session: sessionmaker

    def __init__(self, Model):
        self.g = glb
        self.Model = Model
        self.engine = self.create_engine()
        self.Session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    def create_engine(self):
        return create_async_engine(
            settings.POSTGRES_DATABASE_URI,
            echo=True,
        )

    def create_all(self, connection):
        return self.Model.metadata.create_all(bind=connection)

    def drop_all(self, connection):
        return self.Model.metadata.drop_all(bind=connection)

    @property
    def session(self) -> AsyncSession:
        if not self.g.session:
            self.g.session = self.Session()
        return self.g.session
