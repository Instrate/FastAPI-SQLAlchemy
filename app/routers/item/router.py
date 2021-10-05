from typing import List
from fastapi import Path
from fastapi.param_functions import Depends
from app.database.session import SessionLocal, get_db

import crud

from routers.router import router

from database.schemas import item

# @router.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]

# @router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}

# @router.get("/users/{username}", tags=["users"])
# async def read_user(username:str = Path(...)):
#     return {"username": username}

@router.post("users/{user_id}/items/", response_model=item.Item)
def create_item_for_user(user_id:int, item: item.ItemCreate, db: SessionLocal = Depends(get_db)):
    return crud.create_item_for_user(db=db, item=item, user_id=user_id)

@router.get("/items/", response_model=List[item.Item])
def read_items(skip:int=0, limit:int=0, db: SessionLocal = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items