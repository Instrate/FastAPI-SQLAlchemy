from typing import List
from fastapi import Path, HTTPException, APIRouter
from fastapi.param_functions import Depends
from database.session import SessionLocal, get_db

from schemas import user

import crud

user_router = APIRouter(
    prefix='/user',
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)

@user_router.post("/users/", response_model=user.User)
def create_user(user: user.UserCreate, db: SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already in use")
    return crud.create_user(db=db, user=user)

@user_router.delete("/users/{user_id}", response_model=user.User)
def delete_user(user_id:int, db: SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)

@user_router.get("/users/", response_model=List[user.User])
def read_users(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@user_router.get("/users/{user_id}", response_model=user.User)
def read_user(user_id:int, db:SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
