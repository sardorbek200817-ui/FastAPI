from fastapi import FastAPI , UploadFile, Form , File , HTTPException
from pathlib import Path
from pydantic import BaseModel, EmailStr
import shutil
from typing import Annotated

# Form va File Html uchun chunki Hmtl dagi 
# malumot Form va File orqali keladi Jsoni tushinmaydi

# username:str = Form() >>>>> malumot Form oqali keladi
# username:str  >>>> JSON orqali keladi


app = FastAPI()


UPLOAD_DIR = Path("uploads") # Uplod degan papkaga bizng rasimlarimizni malumotlarimizni saqlaydi
UPLOAD_DIR.mkdir(exist_ok=True) # Upload papkani har safar ochib yubormaslik uchun



@app.post("/upload")
async def Upload(username:str = Form() , password:str = Form() , image : UploadFile  = File()):
    dest = UPLOAD_DIR / image.filename # qaysi papkaga qanday nom bilan saqlanishi kerakligini bildiradi
    
    with open(dest, "wb") as buffer:   
        shutil.copyfileobj(image.file, buffer)   # papkaga saqlaydi va havfsizlik uchun
    return {"img":"ok"}




username:str = Form()  # = Form() chunki html dan Form ichida malumot keladi
image : UploadFile  = File() # = File() chunki html dan File ichida
                             #img jonatiladi , UploadFile oziniki



# 1 ] Nega kerak

# Bularning foydasi html sayitlari bilan tez boglanish 
# filelarni bolaklarga bolish tez uzatish
# va malumotlarni ajratib olish

# 2 ] Mazmuni
 
# Form - File > > > FastApi ga malumotlar qayerdan kelayotkanini va 
# qanday turdagi malumot ekanligini anglatadi



# 3 ]  Formni BaseModel ishlatadiga qilish

# ✔️ To‘g‘ri tushuncha

# Formdan kelgan ma’lumot BaseModelga “aylantiriladi”, keyin BaseModel uni ishlatadi.


class P(BaseModel):
    email: EmailStr
    password: str

@app.post("/login")
async def login(data: Annotated[P, Form()]):
    return data





    # VAZIFA

# POST /auth/login yozing. Form maydonlari: email, password. Email ichida @ bo'lmasa — 400.

@app.post("/vazifa")
async def register(email:str = Form() , password:str = Form()):
    errors = []
    if "@" not in email:
        errors.append({"email":"email hato"})
    if errors:
        raise HTTPException(status_code=400 ,detail=errors)
    
    return {"msg":"ok"}

