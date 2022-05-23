from src.db.init_db import session
from src.db.models import Item
from src.schemas.items.item import Marc_Bibliographic, Items_Model

search = 'deserto'

#items = session.query(Item).filter(Item.title.like("%"+search+"%"))
items = session.query(Item)
item = items.all()[0]

model = Marc_Bibliographic(**item.marc)

x = Items_Model(items=[Marc_Bibliographic(**item.marc) for item in items.all()])