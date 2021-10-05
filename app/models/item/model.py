from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.engine import Base


class Item(Base):
    __tablename__ = 'items_data'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30))
    description = Column(String)
    owner_id = Column(String, ForeignKey("users_accounts.id"))

    owner = relationship("User", back_populates="items")
