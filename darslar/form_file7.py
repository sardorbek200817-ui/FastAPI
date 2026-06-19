from fastapi import FastAPI , UploadFile, Form , File , Response , HTTPException
from pathlib import Path
from pydantic import BaseModel, EmailStr
import shutil
from typing import Annotated

# Buning form_file6 dan farqi bunda kopgina img larni yuklash va saqlash mumkin

# 1 ] rasim va filelarni kop qilib yuklash

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI()


# 0 ] kopgina filelarni yuklash

@app.post("/")
async def Image(image:list[UploadFile]):
 
    return {"name": [file.filename for file in image]} # name larini chiqarish har bir fileni



# 2 ] chegara qoyish yani qaysi file yuklansin qaysi yuklanmasin 
#  ve necha mb dan oshmasin


file_types = [
    "video/mp4" ,"image/jpeg"
]


@app.post("/update")
async def create(file:UploadFile):
    if file.size > 5000000: # 5 mg byteda olchanadi
        raise HTTPException(status_code=400 ,detail="file hajimi kotta")
    elif file.content_type in file_types:
        print("File")
    else:
        print(f"rasim turi {file.content_type}")


# content_type >> file turi
# size >>> file hajimi 

# Hulosa
# 1 ]  file.content_type in file_types:   >>>   file.content_type jamiki UploadFile lar 
# ichidan file_types ichiga kiruvchi file topilsa tru # bolmasa false 


# 2] file.size > 5000000:  >>> agarda file yoki rasimlar 5 mg dan katta bolsa detail ishlaydi bt olchanadi





# vazifa  
# 1 ] fileni tekshirsh

field = [
    "image/png"
]

@app.post("/vazifa")
async def vazifa(pdf:UploadFile = File()):
    if pdf.size <= 10000000 and pdf.content_type in field: # field ichida content_type bormi
        return {"msg":'ok'}
    raise HTTPException(status_code=400 , detail={"msg":"hato"})


# 2 ] demak  for ga solinsa bir nechta filelarni tekshirishi mumkin saqlash yoq

@app.post("/vazifa")
async def nimadir(pdf:list[UploadFile] = File()):
    for i in pdf:
        if i.size <= 10000000 and i.content_type in field: # field ichida content_type bormi
            return {"msg":'ok'}
        raise HTTPException(status_code=400 , detail={"msg":"hato"})
    
    
    
    
# 3 ] endi bu murakkab kopgina filelarni tekshirish va saqlash

@app.post("/nima")
async def Kimdir(pdf:list[UploadFile] = File()):
    for i in pdf:
        if i.size <= 10000000 and i.content_type in field: # field ichida content_type bormi   
            dest = UPLOAD_DIR / i.filename # qaysi papkaga qanday nom bilan saqlanishi kerakligini bildiradi
            
            with open(dest, "wb") as buffer:   
                    shutil.copyfileobj(i.file, buffer)    
                    return {"msg":'ok'}
    raise HTTPException(status_code=400 , detail={"msg":"hato"})
