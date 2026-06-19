from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class Enum(str, Enum):
    student = "student"
    admin = "admin"

students = [
    {"id":1 , "name":"Sarodor" , "baho":5},
    {"id":2 , "name":"Shahodat" , "baho":4},
    {"id":3 , "name":"Jamshid" , "baho":3},
    {"id":4 , "name":"Sarodor Yunsaliyev" , "baho":2},
]

# Enum bu huddi django singari choises kabi ishlaydi buning
# avzallik taraflaridan bir permission qilish mumkin if orqali


@app.get('/student/{student_id}/status/{role}')
async def student(student_id: int , role:Enum):
    if role == Enum.admin:
        for i in students:
            if i["id"] == student_id:
                if i["baho"] == 5 or i["baho"] == 4:
                    return {"admin":"imtihondan otdi" , "student":i}
                elif i["baho"] == 3:
                        return {"admin":"qaytadan imtihon" , "student":i}
                elif i["baho"] == 2:
                    return {"admin":"imtihondan yeqildi" , "student":i}
    elif role == Enum.student:
        for i in students:
            if i["id"] == student_id:
                if i["baho"] == 5 or i["baho"] == 4:
                    return {"student":"imtihondan otdi"}
                elif i["baho"] == 3:
                        return {"student":"qaytadan imtihon"}
                elif i["baho"] == 2:
                    return {"student":"imtihondan yeqildi"}            
    return {"student":"bunday id mavjud emas"}
        
 
                
@app.get("/swager/{role}")
async def student(role:Enum):
    return {"msg":f"siz statusingiz {role.value}"}


# {role.value}   bu qiymatni olib beradim Enum classi ichidangi 
