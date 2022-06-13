from fastapi import APIRouter, Depends, HTTPException
from src.schemas.request.exemplar import Request_Exemplares, Request_Del_Exemplares, Exe_Schema
from src.schemas.response.exemplar import Response_Exemplares
from src.db.init_db import session, engine
from src.db.models import Item, User, Exemplar
#from src.auth.login import get_usuario_logado
from src.auth.current_user import get_current_user
from datetime import date
from sqlalchemy import update

router = APIRouter()

#RETORNA EXEMPLARES DE UM ITEM
@router.get('/{item_id}', response_model= Response_Exemplares)
async def get_exemplares(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    exs = []
    for e in item.exemplares:
        exs.append({
            "id" : e.id,
            "library" : e.library,
            "shelf" : e.shelf,
            "callnumber" : e.callnumber,
            "collection" : e.collection,
            "volume" : e.volume,
            "ex": e.ex,
            "number" : e.number,
            "status" : e.status,
            "created_at": e.created_at
        })

    return Response_Exemplares(exemplares=exs)


#CRIA EXEMPLARES
@router.post('/{item_id}')
async def create_exemplar(
    item_id: int, 
    request: Request_Exemplares,
    auth: User = Depends(get_current_user)):

    item = session.query(Item).filter_by(id = item_id).first()
    exs = request.exemplares
    for ex in exs:
        #print(ex)
        e = Exemplar(
            number = ex.number,
            callnumber = ex.callnumber,
            volume = ex.volume,
            ex = ex.ex,
            library = ex.library,
            shelf = ex.shelf,
            status = ex.status,
            collection = ex.collection
            )
        item.exemplares.append(e)
    session.add(item)
    session.commit()

    return item.exemplares

#ATUALIZA EXEMPLAR
@router.put('/{ex_id}' )#, response_model=Request_Exemplares)
async def patch_exemplar(
    ex_id: int, 
    request: Exe_Schema,
    auth: User = Depends(get_current_user)):

    ex = session.query(Exemplar).filter_by(id = ex_id).first()
    if ex is None:
        raise HTTPException(status_code=404, detail="Exemplar not found")
    
    stmt = (
        update(Exemplar).
        where(Exemplar.id == ex_id).
        values(**request.dict()))
    session.execute(stmt)
    session.commit()    
    
    return {'msg': "Exemplares atualizados com sucesso!"}





#DELETA EXEMPLARES
@router.delete('/{ex_id}')
async def delete_exemplar(
    ex_id: int,    
    auth: User = Depends(get_current_user)):

    ex = session.query(Exemplar).filter_by(id = ex_id).first()
    if ex is None:
        raise HTTPException(status_code=404, detail="Exemplar not found")
    session.delete(ex)
    session.commit()
    
    return {'msg': "Exemplares excluidos com sucesso!"}

    

#RETORNO O PROXIMO EXEMPLAR
@router.get('/next_exemplar/')
async def get_next_exemplar():
    ex = session.query(Exemplar).order_by(Exemplar.id.desc()).first()
    if ex == None:
        return {'exemplar': str(date.today().year)[2:]+'-0001'}

        
    lastEx = str(ex).split("-")
    lastYear = lastEx[0]
    lastNumber = int(lastEx[1])
    currentYear = str(date.today().year)[2:]
    if lastYear == currentYear:
        number = str(lastNumber+1)
        fill = (4 - len(number))* '0'
        return {'exemplar': currentYear+"-"+fill+str(lastNumber+1)}
    else:
        return {'exemplar': currentYear+"-0001"}