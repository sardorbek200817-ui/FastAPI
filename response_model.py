from fastapi import FastAPI
from pydantic import BaseModel , Field , EmailStr

app = FastAPI()

class Student(BaseModel):
    name: str = Field(default="" , max_length=20)
    email: EmailStr
    age : int | None = None
    yili : int

@app.post("/" ,response_model=Student , response_model_exclude={"name" , "email"}) #nima malumot ketmasligi
async def salom(student:Student):
    return student




class Studentlar(BaseModel):
    name: str
    age : int | None = None
    yili : int

    
@app.post("/" ,response_model=Studentlar , response_model_include={"name" , "age"}) # nima malumot ketishi
async def salomlar(student:Student):
    return student


# Agarda bitta modeldan yozmoqchi bolsangiz < response_model_include >  va < response_model_exclude > ishlat
# ular bitta modelda qaysi birini foydalanishni yoki foydalanmaslikni aytadi
