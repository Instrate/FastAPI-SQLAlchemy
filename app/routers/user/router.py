from typing import List
from fastapi import Path, HTTPException
from fastapi.param_functions import Depends
from database.session import SessionLocal, get_db

from database.schemas import user

import crud

from routers.router import router

# @router.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]

# @router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}

# @router.get("/users/{username}", tags=["users"])
# async def read_user(username:str = Path(...)):
#     return {"username": username}


@router.post("/users/", response_model=user.User)
def create_user(user: user.UserCreate, db: SessionLocal):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already in use")


@router.get("/users/", response_model=List[user.User])
def read_users(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    users = crud.get_user(db, skip=skip, limit=limit)
    return users


@router.get("/users/", response_model=user.User)
def read_user(user_id:int, db:SessionLocal = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
