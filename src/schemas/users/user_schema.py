from pydantic import BaseModel, Field, validator
from src.auth.authenticate import get_password_hash
from typing import Optional

class User_Response(BaseModel):
    id: int
    name: str
    email: str
    addressCep: str
    addressCity: str
    addressDistrict: str
    addressNumber: str
    addressStreet: str
    birth: str
    cellphone: str
    sex: str
    surname: str
    vinculo: str
    img: Optional[str]

class Simple_User(BaseModel):
    id: int
    name: str


class User_Request(BaseModel):
    name: str
    email: str
    password: str

class UserCreateRequest(BaseModel):
    name: str
    email: str
    addressCep: str
    addressCity: str
    addressDistrict: str
    addressNumber: str
    addressStreet: str
    birth: str
    cellphone: str
    sex: str
    surname: str
    vinculo: str
    hash_password: str = Field(alias='password')

    @validator('hash_password', pre=True)
    def hash_the_password(cls, v):
        return get_password_hash(v)    