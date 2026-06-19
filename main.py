from fastapi import FastAPI , Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker , Session
from database2 import SessionLocal , Base , engine
from models import Book
from basemodel import BaseModel
from crud import kitob , get_all_boks , delete_book
app = FastAPI()


Base.metadata.create_all(bind=engine) # Bu database ichida jadval yaratadi


# kitoblar = [
#     {'id':1 , "name":"mehrobdan chayon" ,"price":1212 ,"desc":"yaxshi kitob"},
#     {'id':2 , "name":"mehrobdan chayon" ,"price":100 ,"desc":"yaxshi kitob"},
#     {'id':3 , "name":"mehrobdan chayon" ,"price":4444 ,"desc":"yaxshi kitob"},
#     {'id':4 , "name":"mehrobdan chayon" ,"price":5454 ,"desc":"yaxshi kitob"},
# ]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1 ]  kitob qoshish

@app.post("/kitoblar")
async def kitoblar(book_data : BaseModel , db:Session=Depends(get_db)):
    new_book = kitob(db , book_data)
    return new_book

# kitob crudagi funksiya nomi 


# 2 ] bazadagi hamma qoshilgan kitoblarni chiqarish


@app.get("/all_poks")
async def get_boks(db:Session = Depends(get_db)):
    return get_all_boks(db)

# get_all_boks bu crudagi funksiya nomi



# 3 ] kitob ochirish

@app.delete("/delete/{id}")
async def delete(db:Session = Depends(get_db) , book_id = id):
    if delete_book(db , book_id):
        return {"msg":"Ochirildi"}
    return {"msg":"bunday kitob mavjud emas"}

# delete_book crudagi funksiya nomi