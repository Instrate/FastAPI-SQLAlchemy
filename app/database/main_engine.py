from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base



SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:root@127.0.0.1:5432/postgres"


engine = create_engine(url=SQLALCHEMY_DATABASE_URL, echo=True, future=True)

Base = declarative_base()

