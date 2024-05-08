from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.base.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    fullname = Column(String)
    avatar = Column(String)
    