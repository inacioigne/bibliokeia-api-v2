from fastapi import APIRouter, Depends, HTTPException
from src.schemas.items.item import Marc_Bibliographic, Items_Model, Item_Model
from src.db.init_db import session
from src.db.models import Item


router = APIRouter()

#Get items
@router.get('/items', response_model= Items_Model)
async def get_item():
    items = session.query(Item).all()

    all_items = Items_Model(items=[Item_Model(marc=Marc_Bibliographic(**item.marc), id=item.id ) for item in items])

    return all_items