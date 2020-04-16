from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from tifa.globals import db


class Item(db.Model):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
