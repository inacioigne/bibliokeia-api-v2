from pydantic import BaseModel
from typing import Dict, List


class Marc_Bibliographic(BaseModel):
    leader: str
    controlfields: Dict
    datafields: Dict

class Field_Marc(BaseModel):
    tag: str
    subfields: Dict

class Item_Model(BaseModel):
    id: int
    marc: Marc_Bibliographic

class Items_Model(BaseModel):
    items: List[Item_Model]
