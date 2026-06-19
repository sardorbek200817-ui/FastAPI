# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# from datetime import datetime
# from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey

# from datetime import datetime
# from pydantic import BaseModel, EmailStr
# from sqlalchemy.orm import Session
# from fastapi import FastAPI

# app = FastAPI()

# DATABASE_URL = "sqlite:///./app.db"
# # PostgreSQL: "postgresql://user:pass@localhost/dbname"

# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False},  # faqat SQLAlchemy ni database ga ulaydigan narsa
# )

# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base = declarative_base()



# class Post(Base):
#     __tablename__ = "Posts"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     content = Column(String, nullable=False)
    


# class PostBase(BaseModel):
#     title: str
#     content: str


# class PostCreate(PostBase):
#     pass


# def create_post(db: Session, data: PostCreate) -> Post:
#     post = Post(**data.model_dump())
#     db.add(post)
#     db.commit() # query ni bajarish
#     db.refresh(post)
#     return post


# @app.post("/database")
# async def database():
#     return {"msg":"ishladi"}


# primary_key=True id asosiy kalit bolsin   index = True qidiruvni tezlashtirish uchun
# String bu djangodagi charfield    unique = True yaratilgan email qayta yana yaratilmasin yani u faqat 1 ta bolsin
# nullable=False > bu bosh bolib qolmasin






from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Bu funksiya foydalanuvchidan kelgan post (title, content) ma’lumotini 
# olib, databasega saqlaydi va saqlangan postni qaytaradi.

app = FastAPI()

# Database
DATABASE_URL = "sqlite:///./app.db" # Bu SQLAlchemy'ga:
                                    # "app.db nomli SQLite database bilan ishlaymiz"


engine = create_engine( # database bilan gaplashish yoli huddi djangodagi orm kabi
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker( # databasega ulan
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base() # Men yaratadigan klasslarni database jadvaliga aylantir


# Model
class Post(Base):
    __tablename__ = "posts" # database ichidagi jadval nomi

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)


# primary_key=True id asosiy kalit bolsin   index = True qidiruvni tezlashtirish uchun
# String bu djangodagi charfield    unique = True yaratilgan email qayta yana yaratilmasin yani u faqat 1 ta bolsin
# nullable=False > bu bosh bolib qolmasin


# Jadval yaratish
Base.metadata.create_all(bind=engine) # modellarni database ichida JADVAL (table) qilib yaratadi


# Schema
class PostCreate(BaseModel):
    title: str
    content: str


# Post yaratish funksiyasi  bu funksiya malumotlarni databasega saqlashga javob beradi
def create_post(data: PostCreate):
    db = SessionLocal() # databasega ulanish

    post = Post(
        title=data.title,
        content=data.content
    )

    db.add(post) # malumot qay tartibda qoshilishi masalan malumot qoshish 
    # uchun post ishlatamiz ozgartirish uchun Put yoki Patch
    db.commit() # query ni bajarish barcha o‘zgarishlarni REAL databasega yozib qo‘y
    db.refresh(post) # databasega yangi malumot kirib kelsa olib keladi
    db.close() # Database bilan aloqani yop ram tejash

    return post


# Test route serverni tekshirib olish
@app.get("/")
async def home():
    return {"message": "API ishlayapti"}


# Databasega post yozish databasedagi malumotlarimizni chiqaryabmiz
@app.post("/posts")  
async def add_post(create: PostCreate):
    post = create_post(create) # create ichiga yozgan malumotimizni create_post
                               # orqali databasega yozib beradi yani create_postni 
                               # funksiyasini ishlatib yuboradi
    return {
        "id": post.id,
        "title": post.title,
        "content": post.content
    }