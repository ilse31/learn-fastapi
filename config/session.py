from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from .db import settings


DB_URL = settings.DATABASE_URL
print("Database URL is ",DB_URL)
engine = create_engine(DB_URL)



SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

if __name__=="__main__":
    print(DB_URL)
    print(engine)
    print(SessionLocal)