import re

import sqlalchemy as sa
from sqlalchemy.orm import as_declarative, declared_attr, Mapped


def camel_to_snake_case(name: str):
    name = re.sub(r"((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))", r"_\1", name)
    return name.lower().lstrip("_")


@as_declarative()
class BaseModel:
    id = sa.Column(sa.Integer, primary_key=True)

    @declared_attr  # type: ignore
    def __tablename__(cls):
        return camel_to_snake_case(cls.__name__)

    @property
    def class_name(self) -> str:
        """Shortcut for returning class name."""
        return self.__class__.__name__
