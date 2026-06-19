from fastapi import FastAPI
from enum import Enum
app = FastAPI()


       
@app.get("/ism/{ism}") # bu qismi path
async def ism1(ism: str):
    return {"msg":f"Salom {ism}"}
#  'http://127.0.0.1:8000/ism/sardor' \



@app.get("/ism1")
async def ism2(ism: str):  # pathsiz query ning ozi  
    return {"msg":f"Salom {ism}"}
#   'http://127.0.0.1:8000/ism?ism=Ali' \




class Student(str , Enum):
    admin = "admin"
    student = "student"
    teacher = "techer"

    
student_in = [
    {"id":1 , "full_name":"Sardorbek" , "grade":5,"username":"Sardorbek1" , "password":1111},
    {"id":2 , "full_name":"Jahongir" , "grade":3,"username":"Jahongir2" , "password":2222},
    {"id":3 , "full_name":"Mavluda" , "grade":2,"username":"Mavluda3" , "password":3333},
    {"id":4 , "full_name":"Moxinahon" , "grade":4,"username":"Moxinahon4" , "password":4444},
]     
    

@app.post("/student/{type}") # nega type urls ga yozilyabdi chunki if type == Student.admin: manabu yerda uni 
#  tekshirib olish oson boladi yani urldan type yani kimligi kelsa bas.Nega unda username
# va password yozilmaydi chunki path da ular korinib qoladi 
async def student(username: str , password: int , type:Student):
    for i in student_in:
        if username == i["username"] and password == i["password"]:
            if type == Student.admin:
                return {"SIZ":f"{type.value}" , "student":i}
            elif type == Student.student:  # path dan kelyabdi type Enumdagi actionlar
                return {"SIZ":f"{type.value}" , "grade":i["grade"]} # {type.value} bu Enum actiondagi qilmat
            elif type == Student.teacher:
                return {"SIZ":f"{type.value}" , "full_name":i["full_name"] ,"grade":i["grade"] }
            
    return {"msg":"Hunasa bizni aldama"}
            
# {type.value}  type bu pathdan keluvchi kim sorov yuborayotkanligi valiu Enumdagi type qiymati



# Vazifa         < ................ >

 

# 1 ] TOPSHIRIQ
 
Odamlar = [
    {"id":1,"ismi":"Sardor" , "yoshi":18 , "yashash_hudud":"Qushqonoq"},
    {"id":2,"ismi":"ALi" , "yoshi":22 , "yashash_hudud":"Toshkent"},
    {"id":3,"ismi":"Eshon" , "yoshi":16 , "yashash_hudud":"Samarqand"},
    {"id": 4,"ismi":"Suxrob" , "yoshi":19 , "yashash_hudud":"Namangan"},
]


@app.get("/qidiruv/{id}/{yashash_hudud}")
async def search(id: int , yashash_hudud: str | None = None,):
    for i in Odamlar:
        if i["id"] == id and i["yashash_hudud"] == yashash_hudud:
            return {"Malumotlar":i}
    return {"msg":"Unday malumot yoq"}




# 2 ] TOPSHIRIQ

Kitoblar = [
    {"muallif":"Sardorbek" , "yili":1000},
    {"muallif":"Dostonbek" , "yili":1999},
    {"muallif":"Jamshidbek" , "yili":1300},    
]



@app.get("/kitoblar/{muallif}/{yili}")
async def kitob(muallif: str , yili:int):
    for i in Kitoblar:
        if len(muallif) >= 2 and muallif in i["muallif"] and yili > 999 and i["yili"] == yili:
            return {"kitoblar":i}
    
    return {"msg":"bunday kitob mavjud emas"}


# len(muallif) >= and muallif in i["muadllif"]  bu muallifga 
# kamida 2 ta soz kiritishligini va muallif sozi 
# ichida shu 2 ta soz bormi yoqmi tekshiryabdi
