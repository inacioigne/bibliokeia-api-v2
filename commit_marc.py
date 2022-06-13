from src.db.init_db import session
from src.db.models import Item
import json

def send_marc():
    with open("src\import\json_marc.json", encoding="utf8") as file:
        records = json.load(file)
        file.close()

    for record in records:
        title = record.get("datafields").get("245").get('subfields').get('a')
        item = Item(title = title, marc = record)
        #item.exemplares.append(e)
        session.add(item)
        session.commit() 
    

send_marc()