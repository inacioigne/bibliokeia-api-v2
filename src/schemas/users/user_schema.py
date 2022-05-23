from pydantic import BaseModel, Field, validator
from src.auth.authenticate import get_password_hash

class User_Response(BaseModel):
    id: int
    name: str
    email: str

class User_Request(BaseModel):
    name: str
    email: str
    password: str

class UserCreateRequest(BaseModel):
    name: str
    email: str
    hash_password: str = Field(alias='password')

    @validator('hash_password', pre=True)
    def hash_the_password(cls, v):
        return get_password_hash(v)    