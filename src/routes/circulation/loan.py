from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, List
from src.db.models import User, Loan, Exemplar
from src.db.init_db import session
from src.auth.current_user import get_current_user
from src.schemas.users.user_schema import Simple_User

router = APIRouter()

#Loan
@router.post("/loan/{user_id}")
async def make_loan(
    user_id: int,
    request: List,
    current_user: Simple_User = Depends(get_current_user)):

    log =  {'creator': {'id': current_user.id, 'name': current_user.name }}

    user = session.query(User).filter_by(id = user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    #loan = Loan(log=log)
    
    for register in request:
        loan = Loan(log=log)
        ex = session.query(Exemplar).filter_by(number = register).first()
        if ex is None:
            raise HTTPException(status_code=404, detail="Exemplar not found")
        loans = session.query(Loan).filter_by(status = "Emprestado") \
                .join(Loan.exemplar).filter_by(number = register).all()
        if len(loans) > 0:
            raise HTTPException(status_code=409, detail="Exemplar already loan")

        loan.exemplar = ex
        user.loan.append(loan)
    session.add(user)
    session.commit() 

    return {'msg': 'Emprestimos realzados com sucesso'}

@router.get("/loan/{user_id}")
async def get_loan(
    user_id: int,
    current_user: Simple_User = Depends(get_current_user)):

    loans = session.query(Loan).filter_by(user_id = user_id).filter_by(status = "Emprestado").all()
    if len(loans) == 0:
        raise HTTPException(status_code=404, detail="Não há empréstimos para este usuário")

    emprestimos = list()
    for loan in loans:
        emprestimos.append(
            {
                'title': str(loan.exemplar.item),
                'exemplar': str(loan.exemplar),
                "loan_at": loan.created_at.strftime("%d/%m/%Y"),
                "due": loan.due.strftime("%d/%m/%Y"),
                'status': loan.status
            }
        )

    return emprestimos 


