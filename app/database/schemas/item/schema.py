from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase): pass

class Item(ItemBase):
    id: int
    owner_id: str
    
    class Config:
        orm_mode = True