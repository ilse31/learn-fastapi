from typing import Union

from fastapi import FastAPI,Request, Response
from app.base.base_class import Base
from config.main import engine

def create_tables():
    Base.metadata.create_all(bind=engine) # type: ignore
    
    
def start_application():
    app = FastAPI()
    create_tables()
    return app




app = start_application()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


    

