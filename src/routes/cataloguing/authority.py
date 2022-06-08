from fastapi import APIRouter, Depends, HTTPException
from src.schemas.items.item import Marc_Bibliographic
from src.auth.current_user import get_current_user
from src.schemas.users.user_schema import User_Response
from src.db.models import Authority
from src.db.init_db import session
import httpx
 
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

    doc_solr = {
        'id': authority.id,
        'type': type,
    }
    doc_solr.update(request.dict())


    controlfields = ''
    for i in request.controlfields.keys():
        controlfields = controlfields+f'&f={i}:/controlfields/{i}'


    res = httpx.post(
    f'http://localhost:8983/solr/authority/update/json/docs'\
        '?commit=true',            
    json=doc_solr)


    return {'msg': 'Authority sucessfully', 'solr': res.status_code}



