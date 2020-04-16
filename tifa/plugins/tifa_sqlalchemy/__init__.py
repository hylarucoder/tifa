from pydantic import BaseSettings, PostgresDsn
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from tifa.api import TifaFastApi
from sqlalchemy import inspect


class CustomBaseModel(object):

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    #: Query class used by :attr:`query`. Defaults to
    # :class:`SQLAlchemy.Query`, which defaults to :class:`BaseQuery`.
    query_class = None

    #: Convenience property to query the database for instances of this model
    # using the current session. Equivalent to ``db.session.query(Model)``
    # unless :attr:`query_class` has been changed.
    query = None

    def __repr__(self):
        identity = inspect(self).identity
        if identity is None:
            pk = "(transient {})".format(id(self))
        else:
            pk = ', '.join(str(value) for value in identity)
        return '<{} {}>'.format(type(self).__name__, pk)


class Settings(BaseSettings):
    DATABASE_URI: PostgresDsn = 'postgresql://tifa:tifa@localhost:5432/tifa'


class Plugin:
    def __init__(self, db):
        self.db = db


class TifaSQLAlchemyPlugin:
    """
    inspired by flask-sqlalchemy
    """
    engine: Engine
    Model = declarative_base(cls=CustomBaseModel, name="Model", metadata=None)
    session: Session

    def __init__(self):
        pass

    def setup_plugin(self, app: TifaFastApi):
        app.plugins["sqlalchemy"] = self
        self.engine: Engine = create_engine(app.settings.POSTGRES_DATABASE_URI, pool_pre_ping=True)
        self.session = self.create_scoped_session()

    @property
    def metadata(self):
        """The metadata associated with ``db.Model``."""
        return self.Model.metadata

    def create_scoped_session(self):
        return scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )

    def create_session(self):
        SessionCls = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        return SessionCls()
