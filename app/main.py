from routers import routers

from database import Base, engine, app


Base.metadata.create_all(bind=engine)

for router in routers:
    app.include_router(router)