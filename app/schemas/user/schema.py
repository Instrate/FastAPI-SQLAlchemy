from typing import List, Optional
from pydantic import BaseModel

from ..item import Item

class UserBase(BaseModel):
    username: str
    
class UserCreate(UserBase):
    email: str
    password: str
    
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    
    class Config:
        orm_mode = True