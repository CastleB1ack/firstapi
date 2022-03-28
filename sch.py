from pydantic import BaseModel, EmailStr
from pydantic.types import conint


class p (BaseModel) :
    email: str 
    pas: str
    class Config:
        orm_mode = True
class rp (BaseModel) :
    email:str 
    id : int
    class Config:
        orm_mode = True

class vot(BaseModel):
    pi : int
    vod:conint(ge=0,le=1)

class po (BaseModel):
    class Config:
        orm_mode = True
    id : int
    users: str
    posts: str
    em : str
    owner: rp

class pv (BaseModel):
    pp : po
    vot : int
