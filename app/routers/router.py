from fastapi import APIRouter
from fastapi.param_functions import Depends
from database.session import get_db

ROUTER = APIRouter(
    prefix='/site',
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)