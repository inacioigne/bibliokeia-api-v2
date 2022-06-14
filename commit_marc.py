from src.db.init_db import session
from src.db.models import Item, Exemplar
import json
from datetime import datetime

def send_marc():
    with open("src\import\json_marc.json", encoding="utf8") as file:
        records = json.load(file)
        file.close()

    for record in records:
        title = record.get("datafields").get("245").get('subfields').get('a')
        item = Item(title = title)
        session.add(item)
        session.commit()
        record.get('controlfields')['001'] = item.id
        exemplares = record.get('datafields').get('952')
        record.get('datafields').pop('952')
        item.marc = record
        item.logs = {
            'user': 'Importação automática', 
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
        for exemplar in exemplares:
            e = Exemplar(
                library = "Biblioteca do INPA",
                shelf = record.get('datafields').get('852').get('subfields').get('c'),
                callnumber = record.get('datafields').get('090').get('subfields').get('a'),
                collection = "Obras gerais",
                number = exemplar.get('subfields').get('p'),
                ex = f'Ex. {exemplares.index(exemplar)}',
                status = "Disponível",
                )
            item.exemplares.append(e)
        session.add(item)
        session.commit() 
     

#send_marc()