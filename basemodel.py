from pydantic import BaseModel

class BaseModel(BaseModel):
    id : int
    name: str
    price :int
    desc : str

