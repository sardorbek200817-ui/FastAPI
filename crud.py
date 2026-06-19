from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from models import Book
from database2 import SessionLocal

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# malumot qoshish uchun crud

def kitob(db:Session ,book_data):
    book = Book(**book_data.model_dump())
    db.add(book) # malumot qay tartibda qoshilishi masalan malumot qoshish 
    # uchun post ishlatamiz ozgartirish uchun Put yoki Patch
    db.commit() # query ni bajarish barcha o‘zgarishlarni REAL databasega yozib qo‘y
    db.refresh(book) # databasega yangi malumot kirib kelsa olib keladi
    db.close() # Database bilan aloqani yop ram tejash
    return book


# hamma malumotlarni olish uchun crud

def get_all_boks(db:Session):
    return db.query(Book).all()


# malumotlarni ochirish uchun curd yani database bilan boglanish

def delete_book(db:Session , id:int):
    bookk = db.query(Book).get({"id":id})
    if bookk is not None:
        db.delete(bookk) # kitob topilsa True ishlaydi topilmasa False
        db.commit()
        return True
    
    return False