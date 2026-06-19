from fastapi import FastAPI , HTTPException
from pydantic import BaseModel , Field , EmailStr
from enum import Enum
from pydantic_extra_types.payment import PaymentCardNumber
from pydantic_extra_types.phone_numbers import PhoneNumber , PhoneNumberValidator




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





# Amaliy   yangi amaliy malumotlar



student_in = [
    {"id":1 , "full_name":"Sardorbek" , "grade":5,"username":"Sardorbek1" , "password":1111},
    {"id":2 , "full_name":"Jahongir" , "grade":3,"username":"Jahongir2" , "password":2222},
    {"id":3 , "full_name":"Mavluda" , "grade":2,"username":"Mavluda3" , "password":3333},
    {"id":4 , "full_name":"Moxinahon" , "grade":4,"username":"Moxinahon4" , "password":4444},
]   

class Student1(str ,Enum):
    student = "student"
    admin = "admin"
class Student2(BaseModel):
    id : int
    full_name : str
    grade : int


class Admin(Student2): # 1) Student2 dan vorislik olinyabdi yani Student2 hamma malumot Adminga
    username : str     #  otyabdi lekin admindagi malumot Student2 ga otmaydi
    password :int


@app.get("/yangi")
async def adminstudent(student_id:int ,status:Student1):
    for i in student_in:
        if i["id"] == student_id:
            if status == Student1.admin:
                return Admin(**i)
            else:
                return Student2(**i)
        return {"msg":"nimadir hato"} # kiritilgan malumotlarnig hammsi hato bolsa yani if ishlamasa




# Bu yerda Adminga oid malumotlar va studentga oid malumotlar ajratilib kerakli joyga yonaltirilyabdi
# Student1 va Admin  student_in bazasidan olingan ma'lumotlarni saralash va 
# filterlash (formatlash) uchun chaqirilgan.



#  <<<<<<   Vazifa    >>>>>


# Base model orqali malumot qoshish append()


class Status(str , Enum):
    user = "user"
    admin = "admin"




class ProductCreate(BaseModel):
    id : int
    nomi : str
    malumot : str
    price : float


mahsulotlar = [
]


@app.post("/mahsulotlar")
async def Product(product:ProductCreate):
    mahsulotlar.append(product.model_dump())  # model_dump() malumotlarimizni dict korinishida                                           
    return mahsulotlar                        # tushunarli qilib chiqarib berish



# malumotni ochirish


@app.delete("/{id}")
async def Productdelate(id:int):
    for i in mahsulotlar:
        if i["id"] == id:
            mahsulotlar.remove(i)
            return mahsulotlar
    raise HTTPException(status_code=404, detail="Mahsulot topilmadi")
    
    
    
    
    
