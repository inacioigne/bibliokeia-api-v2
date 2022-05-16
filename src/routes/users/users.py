from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas.response.users import User_Response
from src.auth.current_user import get_current_active_user

router = APIRouter()

@router.get("/me", response_model=User_Response)
async def read_users_me(current_user: User_Response = Depends(get_current_active_user)):
    return current_user