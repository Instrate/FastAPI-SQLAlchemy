from fastapi import Path
from fastapi.param_functions import Depends

from routers.router import router

from database.session import get_db

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}

@router.get("/users/{username}", tags=["users"])
async def read_user(username:str = Path(...), db = Depends(get_db)):
    return {"username": username}