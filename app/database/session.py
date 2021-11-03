from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from .main_engine import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "ws://localhost",
#     "http://localhost:8080",
#     "ws://localhost:4200",
#     "http://localhost:4200"
#     ]

app.add_middleware(
    CORSMiddleware,
    **{"allow_origins": ["*"], "allow_methods": ["*"], "allow_headers": ["*"], "allow_credentials": True}
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal Server Error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

def get_db(request: Request):
    return request.state.db

class Request():
    def table_drop(session: sessionmaker, table_name: str):
        if session and table_name:
            req = text("DROP TABLE IF EXISTS %s" % table_name)
            session.execute(req)

    def table_select(session: sessionmaker, table_name: str):
        if session and table_name:
            req = text("SELECT * FROM %s" % table_name)
            for row in session.execute(req):
                print(row)
