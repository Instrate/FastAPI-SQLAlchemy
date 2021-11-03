from os import system
from typing import List
from fastapi import Path, HTTPException, APIRouter
from fastapi.param_functions import Depends
from fastapi.responses import FileResponse, StreamingResponse
from database.session import SessionLocal, get_db
from models.user.model import User

from schemas import user

import os

import crud

user_router = APIRouter(
    prefix='/user',
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)

@user_router.post("/register/", response_model=user.User)
def create_user(user: user.UserCreate, db: SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already in use")
    return crud.create_user(db=db, user=user)

@user_router.delete("/delete/{user_id}")
def delete_user(user_id:int, db: SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)

@user_router.get("/", response_model=List[user.User])
async def read_users(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@user_router.get("/login/", response_model=user.User)
def login_user(username:str, password:str, db:SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.hashed_password != password:
        raise HTTPException(status_code=404, detail="Wrong password")
    return db_user

@user_router.get("/{user_id}", response_model=user.User)
async def read_user(user_id:int, db:SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.get('/file/photo/', response_class=FileResponse)
async def get_file():
    return FileResponse('./files/photo.png')

@user_router.get("/file/video/", response_class=StreamingResponse)
async def get_video():
    def iterfile():  
        with open('./files/video.mp4', mode="rb") as file_like:  
            yield from file_like  
    return StreamingResponse(iterfile(), media_type="video/mp4")

@user_router.post('/upload/')
async def upload_file():
    return 