from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Salom, FastAPI!"}



@app.post("/books")
def create_book():
    return {"created": True}



news = [
    {"id":"1" ,"title":"""AOSdan QQSga o‘tish chegarasi qariyb 5 mlrd so‘m deb belgilandi va bu miqdor
    BHMga bog‘lab qo‘yildi. Savdo va xizmat ko‘rsatish hamda umumiy ovqatlanishsohalari uchun 6 
    foizlik QQSni nazarda tutuvchi soddalashtirilgan soliq rejimi joriy etilmoqda
    QQS masalasida tadbirkorlarni qiynab kelgan qator muammolarga yechim berildi""",
    "data":"2023-06-01" , "text":"""Kichik biznes subektlarining o‘sishi uchun yanada qulay iqtisodiy va ma’muriy
    shart-sharoitlar yaratish to‘g‘risida” prezident farmoni e’lon qilindi."""} ,
    
    {
    "id":"2" , "title":"""AOSdan QQSga o‘tish chegarasi qariyb 5 mlrd so‘m deb belgilandi va bu miqdor BHMga 
    bog‘lab qo‘yildi. Savdo va xizmat ko‘rsatish hamda umumiy ovqatlanishsohalari uchun 6 foizlik QQSni nazarda tutuvchi 
    soddalashtirilgan soliq rejimi joriy etilmoqda. QQS masalasida tadbirkorlarni qiynab kelgan qator muammolarga yechim berildi""",
    
    "data":"2023-06-10" , "text":"""Kichik biznes subektlarining o‘sishi uchun yanada qulay iqtisodiy va ma’muriy
    shart-sharoitlar yaratish to‘g‘risida” prezident farmoni e’lon qilindi."""
    }
    
    
]  


@app.get("/yangilar")
async def salom():
    return news


@app.post("/append/{id}/{title}/{data}/{text}") 
#   url orqali kelganlarni olyabmiz:
# malumot qoshish uchun bizga nima nima kerakligi

# URL orqali kelgan qiymatlarni olib, funksiyaga uzatyapmiz. Keyin shu 
# qiymatlardan foydalanib news ro'yxatiga yangi ma'lumot qo'shyapmiz.     
# aynan shu newsda  {id}/{title}/{data}/{text} shu qiymatlar borligi uchun olyabmiz
# va shu malumotlarga ozimizni malumotimizni qoshyabmiz

async def append_news(id: int , title , data , text):
    
    # funksiya qabul qiladigan qiymatlar id title data text shularni qabul qilishini aytyabmiz
    # Sizning misolingizda bu 4 ta qiymatni FastAPI URL'dan olib kelib shu parametrlarga joylashtiradi.
    
    news.append(
        {"id":id , "title":title , "data":data , "text":text}
    )
    return news



@app.get("/router/{id}")
async def router(id):
    for i in news:
        if i["id"] == id:
            return i
    return {"message":"bunday id yoq"}




# Delate qismi

@app.delete("/delete/{id}")

async def delete(id):
    for i in news:
        if i["id"] == id:
            news.remove(i)     
            return news

    return {"msg": f"Topilmadi {id}"}
