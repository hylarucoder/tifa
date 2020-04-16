from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from tifa.settings import get_settings


class CustomBase(object):

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)

engine: Engine = create_engine(get_settings().POSTGRES_DATABASE_URI, pool_pre_ping=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
