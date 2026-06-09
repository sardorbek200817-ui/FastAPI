# 1 ]  Pydantic

# Pydantic klient yozgan (yoki yuborgan) tartibsiz ma'lumotlarni qat'iy 
# tartibga soladi, tozalaydi va sen xohlagan qolipga (shaklga) keltiradi.


# 2 ]  Requestbody

# Request so‘zining o‘zbekcha tarjimasi ham aynan "So‘rov" yoki "Murojaat" degani.
# Xuddi sen aytgandek, mexmon (klient) serverga o‘zining istaklarini, buyurtmalarini so‘rov 
# ko‘rinishida yuboradi. Server esa o‘sha so‘rovni ko‘rib chiqib, unga javob (Response) qaytaradi.

# 3 ] Pydentic validatsiya qila oladi yani malumotlarimizni tekshirish qobilyatiga ega

# $ ASOSIY == > Bizning backendimizga JSON malumot kelganda FastAPI uni qay tartibda 
# kelayotkanini tushinmaydi Pydentic esa shu malumotni FastAPI tushinadiga shaklga keltirib beradi 
# drf mavzudagi serializerni ornini bosadi deb tushinsak ham boladi


from fastapi import FastAPI
from pydantic import BaseModel , Field , EmailStr
from pydantic_extra_types.payment import PaymentCardNumber
from pydantic_extra_types.phone_numbers import PhoneNumber

app = FastAPI()

class User(BaseModel):
    name: str = Field(max_length=20)
    email: EmailStr  # faqat email yozish uchun ruxsat
    age: float = Field(gt=3 , le=100)
    card_number: PaymentCardNumber
    description: str = Field(default="", max_length=500) #ixtiyori yozilsin agarda yozilsa 500 max bolsin
    age: int | None = None    # Ixtiyoriy, default None



@app.post("/")
async def body(user:User):
    print(user.card_number.brand)
    return {"msg":f"Malumotlar qaytdi" , "msg":user}


# Vazifa


class Student(BaseModel):
    name: str = Field(default="" , max_length=20)
    email: EmailStr
    age : int | None = None
    yili : int
    phone_number : PhoneNumber


@app.post("/vazifa")
async def vazifa(student: Student):
    
    return {"msg":student}


