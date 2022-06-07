from fastapi import APIRouter, Depends, HTTPException
from src.schemas.items.item import Marc_Bibliographic
from src.auth.current_user import get_current_user
from src.schemas.users.user_schema import User_Response
from src.db.models import Authority
from src.db.init_db import session

router = APIRouter()

@router.post('/{type}', status_code=201)
async def create_authority(
    type: int,
    request: Marc_Bibliographic,
    current_user: User_Response = Depends(get_current_user)):

    log =  {'creator': {'id': current_user.id, 'name': current_user.name }}

    authority = Authority(log = log, marc = request.dict(), type = type)
    session.add(authority)
    session.commit()

    return {'msg': 'Authority sucessfully'}



