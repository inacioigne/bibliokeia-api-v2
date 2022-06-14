from pydantic import BaseModel
from typing import Dict, List, Optional


class Marc_Bibliographic(BaseModel):
    leader: str
    controlfields: Dict
    datafields: Dict

class Field_Marc(BaseModel):
    tag: str
    subfields: Dict

class Item_Model(BaseModel):
    id: int
    img: Optional[str]
    marc: Marc_Bibliographic

class Items_Model(BaseModel):
    items: List[Item_Model]

class Items_By_Exemplar(BaseModel):
    title: str
    exemplar: str

