from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base

import uuid

class User(Base):
    __tablename__ = 'users_accounts'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String, default=lambda: str(uuid.uuid4()), nullable=True)
    username = Column(String(30), unique=True, index=True)
    email = Column(String(30), unique=True, index=True)
    full_name = Column(String, default='newbuy')
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    items = relationship("Item", back_populates="owner")