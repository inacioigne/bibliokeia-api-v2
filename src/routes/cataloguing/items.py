from fastapi import APIRouter, Depends, HTTPException, UploadFile
from src.schemas.items.item import Marc_Bibliographic, Field_Marc
from src.schemas.users.user_schema import User_Response
from src.auth.current_user import get_current_user
from src.db.models import Item
from src.db.init_db import session
from copy import deepcopy
from datetime import datetime
import shutil
from fastapi.responses import FileResponse

router = APIRouter()

#Create a item
@router.post('/create', status_code=201)
async def create_item(
    request: Marc_Bibliographic, 
    #auth: User = Depends(get_usuario_logado)
    current_user: User_Response = Depends(get_current_user)):
    
    log =  {'creator': {'id': current_user.id, 'name': current_user.name }}
    #Get title
    if  '245' in request.datafields.keys():
        title = request.datafields.get("245").get('subfields').get('a')
    else: 
        raise HTTPException(status_code=404, detail="Title not found")
    
    item = Item(title = title, marc = request.dict(), logs = log)   

    session.add(item)
    session.commit() 

    return {'item_id': item.id, 'marc': item.marc}

#Get item marc
@router.get('/{item_id}', response_model= Marc_Bibliographic)
async def get_item(item_id: int ):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return Marc_Bibliographic(**item.marc)

#Update (Patch) item
@router.patch('/{item_id}', response_model= Marc_Bibliographic)
async def patch_item(
    item_id: int, 
    request: Field_Marc, 
    current_user: User_Response = Depends(get_current_user)):

    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    
    #Update Logs
    logs = deepcopy(item.logs)
    if 'updates' in logs.keys():
        logs.get('updates').append({
            'user': {'id': current_user.id, 'name': current_user.name },
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")})
    else:
        logs['updates'] = [{
            'user': {'id': current_user.id, 'name': current_user.name },
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")}]
    item.logs = logs

    marc = deepcopy(item.marc)
    marc.get('datafields').get(request.tag)['subfields'] = request.subfields
    #handle time
    t = datetime.now()
    time = t.strftime('%Y%m%d%H%M%S')+'.'+t.strftime('%f')[0]  
    marc.get('controlfields')['005'] = time

    item.marc = marc
    session.add(item)
    session.commit()

    return Marc_Bibliographic(**item.marc)

@router.put('/{item_id}', response_model= Marc_Bibliographic)
async def put_item(
    item_id: int, 
    request: Marc_Bibliographic, 
    #auth: User = Depends(get_usuario_logado))
    current_user: User_Response = Depends(get_current_user)):

    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    #Update Logs
    # logs = deepcopy(item.logs)
    # if 'updates' in logs.keys():
    #     logs.get('updates').append({
    #         'user': {'id': current_user.id, 'name': current_user.name },
    #         "date": datetime.now().strftime("%d/%m/%Y %H:%M")})
    # else:
    #     logs['updates'] = [{
    #         'user': {'id': current_user.id, 'name': current_user.name },
    #         "date": datetime.now().strftime("%d/%m/%Y %H:%M")}]
    # item.logs = logs

    item.marc = request.dict()

    return Marc_Bibliographic(**item.marc)

#Imagems
@router.post("/{item_id}/imagem", status_code=201)
async def upload_imagem(item_id: int, file: UploadFile):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    format = file.content_type.split('/')[1]
    path_img = f'./storage/items/{item_id}.{format}'

    with open(path_img, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    item.img = path_img
    session.add(item)
    session.commit()

    return {"filename": path_img }

@router.get("/{item_id}/imagem")
async def get_imagem(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
   
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    elif item.img is None:
        #raise HTTPException(status_code=404, detail="Item without imagem")
        return FileResponse("./storage/items/default.png")

    return FileResponse(item.img)
