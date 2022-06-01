from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, List
from src.db.models import User, Loan, Exemplar
from src.db.init_db import session
from src.auth.current_user import get_current_user
from src.schemas.users.user_schema import Simple_User

router = APIRouter()

@router.post("/devolution/{user_id}")
async def loan(
    user_id: int,
    request: List,
    current_user: Simple_User = Depends(get_current_user)):

    pass
