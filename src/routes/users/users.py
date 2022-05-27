from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from src.schemas.users.user_schema import User_Response, User_Request, UserCreateRequest
from src.auth.current_user import get_current_active_user, get_current_user
from src.db.init_db import session
from src.db.models import User
import shutil

router = APIRouter()

# @router.get("/me", response_model=User_Response)
# async def read_users_me(current_user: User_Response = Depends(get_current_active_user)):
#     return current_user

@router.get('/current_user')
async def currrent_user(current_user: User_Response = Depends(get_current_user)):
    return current_user

@router.get('/{user_id}', response_model= User_Response)
async def get_item(user_id: int ):
    user = session.query(User).filter_by(id = user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return User_Response(**user.__dict__) 



@router.post("/register",status_code=201)# response_model=User_Response, )
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

@router.post("/imagem", status_code=201)
async def create_upload_file(file: UploadFile):
    with open(f'./storage/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)


    return {"filename": file.filename}

    