from inspect import getmembers

from fastapi import FastAPI

from routers import routers

from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()



for router in routers:
    app.include_router(router)