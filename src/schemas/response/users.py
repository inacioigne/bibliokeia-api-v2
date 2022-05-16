from pydantic import BaseModel

class User_Response(BaseModel):
    id: int
    name: str
    email: str