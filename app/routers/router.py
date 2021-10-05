from fastapi import APIRouter
from fastapi.param_functions import Depends
from dependencies import get_token_header
from database.session import get_db

router = APIRouter(
    prefix='/site',
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)