from typing import List
from fastapi import Path, APIRouter
from fastapi.param_functions import Depends
from database.session import SessionLocal, get_db

import crud

from schemas import item

item_router = APIRouter(
    prefix='/item',
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)

@item_router.post("/users/{user_id}/items/", response_model=item.Item)
def create_item_for_user(user_id:int, item: item.ItemCreate, db: SessionLocal = Depends(get_db)):
    item = crud.create_item_for_user(db=db, item=item, user_id=user_id)
    # SessionLocal.add(item)
    # SessionLocal.commit()
    return item

@item_router.get("/items/", response_model=List[item.Item])
def read_items(skip:int=0, limit:int=0, db: SessionLocal = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items