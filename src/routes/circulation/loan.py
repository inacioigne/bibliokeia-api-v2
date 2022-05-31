from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, List
from src.db.models import User, Loan, Exemplar
from src.db.init_db import session
from src.auth.current_user import get_current_user
from src.schemas.users.user_schema import Simple_User

router = APIRouter()

#Loan
@router.post("/loan/{user_id}")
async def loan(
    user_id: int,
    request: List,
    current_user: Simple_User = Depends(get_current_user)):

    user = session.query(User).filter_by(id = user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    loan = Loan()
    user.loan.append(loan)
    for register in request:
        ex = session.query(Exemplar).filter_by(number = register).first()
        if ex is None:
            raise HTTPException(status_code=404, detail="Exemplar not found")
        loan.exemplares.append(ex)
    session.add(user)
    session.commit()

    return {'msg': 'Emprestimos realzados com sucesso'}

