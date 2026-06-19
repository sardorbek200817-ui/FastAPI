from fastapi import FastAPI , HTTPException
from pydantic import BaseModel , Field , EmailStr

app = FastAPI()

# Eror handling foydalanuvchi kiritgan sorovi topilmasa unga hato nimada ekanligini korsatib berish


users = {1: "Ali", 2: "Vali"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")
    return {"user": users[user_id]}


# raise huddi return kabi lekin u hatolar uchun





# 2 ] Ikkinchi AMALIYOT


@app.post("/register")
def register(email: str, password: str):
    errors = []
    if "@" not in email:
        errors.append({"field": "email", "message": "Noto'g'ri email"})
    if len(password) < 8:
        errors.append({"field": "password", "message": "Kamida 8 belgi"})
    if errors: # agarda erros ga biron bir malumot qoshilgan bolsa 
               # chiqaradi yani hato malumot kiritilgan bolsa
        raise HTTPException(400, detail={"errors": errors}) # bu hatolarni ushlaydi yani 
                        # malumot hato kiritilganda yoki topilmaganda  
    return {"ok": True}


# Mening tushinganim

# 1 ) # paroldami yoki email kiritishdami hato kiritb 
# qoysak errors ga yigib beradi va hato qayerda ekanligini korsatadi


#    MAZMUNI

# 1 ) Emailni tekshiradi: Agar @ belgisi qolib ketgan boʻlsa, shart bajariladi va errors 
# roʻyxatiga (ya'ni xatoliklar qutisiga) email haqidagi xabarni qoʻshadi.

# 2 ) Parolni tekshiradi: Agar parol 8 tadan kam boʻlsa, u haqidagi 
# xabarni ham oʻsha xatoliklar qutisiga qoʻshadi.

# 3 ) Oxirida tekshiradi: Agar u qutining ichida (errorsda) biron narsa yigʻilib qolgan
# boʻlsa, oʻsha zaxiraga yigʻilgan xatolarni raise orqali birdaniga tashqariga chiqarib (otib) beryapti.

