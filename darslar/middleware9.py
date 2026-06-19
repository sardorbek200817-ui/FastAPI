from fastapi import Depends, FastAPI,Query , HTTPException , Response
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from collections import defaultdict
from fastapi.responses import JSONResponse

app = FastAPI()


# yuborilgan va request larni qancha vaqtda kelganini bilish va 
# ketganini bilishi yoli bunisi kelgan requestni


@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.time() - start:.3f}"
    return response


# request larga cheklov qoyish yani


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://mysite.com"],  # faqat shu manzildan kelsa response 
    allow_credentials=True,                                         # qaytadi boshqa manzildan javob qaytmaydi
    allow_methods=["*"],
    allow_headers=["*"],
)



# Bizning serverimizga response kelsa agarda u 5 tadan ortib ketsa
# hato qaytaradi . MISOL


@app.post("/yangi")
async def yang():
    return {"msg":"yaxshi"}


request_log = {} # kalit soz orqali qiymatni chaqirib olishi uchun shuning uchun {} foydalanilyabdi

Block_list = [
    
]


LIMIT = 5
MAX = 60       # daqiqada maksimum
WINDOW = 60    # soniyalarda

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    ip = request.client.host # serverga yuborgan har bi request sorovini ip manzilini aniqlab turish
    # agarda yangi sorov kelsa bu ip manzilni request_log = {} avtomatik qoshib qoyadi python

    # 1. IP yangi bo‘lsa boshlaymiz
    if ip not in request_log:# Agar request_log ichida bu IP YO‘Q 
        request_log[ip] = 0  # bo‘lsa, undagi sorovlarni 0 qilib yarat

    # 2. Limitni tekshiramiz
    if request_log[ip] >= LIMIT:
        if ip is not Block_list: # agarda ip block listda bolmasa
            Block_list.append(ip)

        return JSONResponse(
                    status_code=429, 
                    content={"detail": f"Siz bloklandingiz. Blok ro'yxati: {Block_list}"}
                )


    # 3.agarda limit ishlamasa yani request 5 tadan oshib ketmasa requesrga +1 qoshib ket degani har sorovda 
    request_log[ip] += 1  # requestlar soniga 1 ni qoshib ketish

    return await call_next(request) #call_next(request) o'sha yuborilgan narsani ichkariga yuborish
# yani middlewarega sorov yuboradi keyin middlevare uni qabul qilib serverga yuboradi
# call_next = keyingisi


# await — “shu ish tugaguncha kutaman, lekin server boshqa yani async ishlashini taminlab beradi
# requestlarni ham bir vaqtning o‘zida davom ettiradi” degani.

# call_next ning vazifasi — request'ni keyingi bosqichga uzatish.

# Client → Middleware → call_next → Endpoint → Response → Middleware → Client


