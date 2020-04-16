from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from tifa.globals import db


class User(db.Model):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    not_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
