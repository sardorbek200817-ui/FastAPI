from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


# Database
DATABASE_URL = "sqlite:///./app.db" # Bu SQLAlchemy'ga:
                                    # "app.db nomli SQLite database bilan ishlaymiz"


engine = create_engine( # database bilan gaplashish yoli huddi djangodagi orm kabi
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker( # databasega ulanish huddi djangodagi orm kabi boladi
    bind=engine,
    autoflush=False,
    autocommit=False
)




