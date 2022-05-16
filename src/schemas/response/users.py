from pydantic import BaseModel

class User_Response(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None