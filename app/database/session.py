from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from engine import engine


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as ex:
        print(f"Raised: {ex}")
    finally:
        db.close()

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
            