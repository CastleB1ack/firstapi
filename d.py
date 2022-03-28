from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

l = "postgresql://postgres:fucknodejs2700@localhost/test"

e = create_engine(l)

s = sessionmaker(autocommit=False, autoflush=False, bind=e)

b = declarative_base()

def get_db():
    db = s()
    try:
        yield db
    finally:
        db.close()