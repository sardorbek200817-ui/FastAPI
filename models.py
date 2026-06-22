
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker , Session
from database2 import SessionLocal , Base , engine

Base = declarative_base() # Base modellarni SQLAlchemy tushunadigan formatga bog‘laydi

class Book(Base):
    __tablename__ = "book" # database ichidagi jadval nomi

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    desc = Column(String, nullable=False)


## 1 ]  *primary_key = True*  asosiy kalit deb kiritish masalan id

## 2 ]  *index = True* qidiruvni tezlashtirish

## 3 ]  *string* - Djangodagi CharField kabi …

## 4 ]  *nullable = False*  malumotni kiritish shart belgisi
