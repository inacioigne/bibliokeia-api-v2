#from atexit import register
from fastapi import APIRouter, Depends, HTTPException
from src.schemas.items.item import Marc_Bibliographic, Items_Model, Item_Model, Items_By_Exemplar
from src.db.init_db import session
from src.db.models import Item, Exemplar


router = APIRouter()

#Get items
@router.get('/item/items', response_model= Items_Model)
async def get_item():
    items = session.query(Item).all()

    all_items = Items_Model(items=[Item_Model(marc=Marc_Bibliographic(**item.marc), id=item.id ) for item in items])

    return all_items

#Get Exemplares
@router.get("/exemplar/{register}", response_model=Items_By_Exemplar)
async def get_item_by_exemplar(register: str,):
    ex = session.query(Exemplar).filter_by(number = register).first()
    if ex is None:
        raise HTTPException(status_code=404, detail="Exemplar not found")
        
    return Items_By_Exemplar(title=ex.item.title, exemplar=register)