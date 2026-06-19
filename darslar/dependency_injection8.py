from fastapi import Depends, FastAPI, Query
import time
from fastapi import FastAPI, Request


app = FastAPI()


# Sahifalash

products = [
    {"id":1 , "name":"telefon" , "price":213},
    {"id":2 , "name":"texnika" , "price":223},
    {"id":3 , "name":"sabzavotlar" , "price":211},
    {"id":4 , "name":"mevalar" , "price":565},
    {"id":5 , "name":"kiyimlar" , "price":3423},
    {"id":6 , "name":"novtboklar" , "price":432},
    {"id":7 , "name":"pultlar" , "price":345},
    {"id":8 , "name":"robotlar" , "price":656},
]

# page = qaysi sahifa
# per_page = har sahifada nechta malumot borligi
# skip = osha sahifagacha nechta malumot otkazib yuborish kerak
# ge -- kotta    le -- kichik

def pagination(
    page: int = Query(1, ge=1), # standart holatda 1 ta boladi lekin 1 dan kichik bolmasin deyabdi
    per_page: int = Query(10, ge=1, le=100), # ge 1 dan katta le kichik 
):
    return {
        "page": page,
        "per_page": per_page,
        "skip": (page - 1) * per_page,
    }


@app.get("/products")
def products(pg = Depends(pagination)):
    return {"pagination": pg, "products":products}

