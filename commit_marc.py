from src.db.init_db import session
from src.db.models import Item, Exemplar
#from src.solr.acervo.indexing import index_solr  
import json
from datetime import datetime
import httpx

pathfile = 'src\import\E1\P1\marc.json'

item_split = '?commit=true'\
            'split=/'\
                '&f=id:/controlfields/001'\
                    '&f=title:/datafields/245/subfields/a'\
                        '&f=responsibilities:/datafields/245/subfields/c'\
                        '&f=author:/datafields/100/subfields/a'\
                            '&f=publisher:/datafields/260/subfields/b'\
                                '&f=year:/year'\
                                    '&f=serie:/datafields/490/subfields/a'\
                                        '&f=termo_topico:/datafields/650/subfields/a'\
                                               '&f=type:/datafields/900/subfields/a'
def indexing_solr(record, item_split=item_split):
    year = record.get('datafields').get('260').get('subfields').get('c')[:4]
    if year:
        record['year'] = int(year)
    solr = httpx.post(
    f'http://localhost:8983/solr/acervo/update/json/docs{item_split}', json=record)
    print(solr, record.get('controlfields')['001'] )

    
def send_marc(pathfile=pathfile):
    with open(pathfile, encoding="utf8") as file:
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
        
        indexing_solr(record)
        
        for exemplar in exemplares:
            e = Exemplar(
                library = "Biblioteca do INPA",
                shelf = record.get('datafields').get('852').get('subfields').get('c'),
                callnumber = record.get('datafields').get('090').get('subfields').get('a'),
                collection = "Obras gerais",
                number = exemplar.get('subfields').get('p'),
                ex = f'Ex. {exemplares.index(exemplar)+1}',
                status = "Disponível",
                )
            item.exemplares.append(e)
        session.add(item)
        session.commit() 
     

#send_marc()