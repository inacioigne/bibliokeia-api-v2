from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas.users.user_schema import User_Response, User_Request, UserCreateRequest
from src.auth.current_user import get_current_active_user, get_current_user
from src.db.init_db import session
from src.db.models import User

router = APIRouter()

# @router.get("/me", response_model=User_Response)
# async def read_users_me(current_user: User_Response = Depends(get_current_active_user)):
#     return current_user

@router.get('/current_user')
async def currrent_user(current_user: User_Response = Depends(get_current_user)):
    return current_user

@router.post("/register", response_model=User_Response, status_code=201)
async def register(request_user: UserCreateRequest):
    user = session.query(User).filter_by(email = request_user.email).first()
    if user:
        raise HTTPException(status_code=409,
                            detail="Email ja cadastrado"
                           )
                           
    atributos = request_user.dict(exclude_unset=True)
    user = User(**atributos)
    session.add(user)
    session.commit()

    return  {'id':user.id,'name':user.name,'email':user.email}
    