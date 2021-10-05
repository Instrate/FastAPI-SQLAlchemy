from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.engine import Base

class Item(Base):
    __tablename__ = 'items_data'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30))
    description = Column(String)
    owner_id = Column(String)
    
    owner = relationship("User", back_populates="items")