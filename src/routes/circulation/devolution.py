from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, List
from src.db.models import User, Loan, Exemplar
from src.db.init_db import session
from src.auth.current_user import get_current_user
from src.schemas.users.user_schema import Simple_User
from copy import deepcopy
from datetime import datetime

router = APIRouter()

@router.post("/devolution/{register}")
async def loan(
    register: str,
    current_user: Simple_User = Depends(get_current_user)):

    loans = session.query(Loan).filter_by(status = "Emprestado") \
        .join(Loan.exemplar).filter_by(number = register).all()

    for loan in loans:
        loan.status = "Devolvido"
        log = deepcopy(loan.log)
        log['devolution'] = {
            'id':  current_user.id, 
            'name': current_user.name, 
            'date': datetime.now().strftime("%d/%m/%Y %H:%M") }
        loan.log = log
    session.add_all(loans)
    session.commit()
        

    return {'mgs': 'exemplar devolvido com sucesso"'}
