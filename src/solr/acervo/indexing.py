import httpx
import json

pathfile = 'src\import\json_marc.json'

with open(pathfile, encoding="utf8") as file:
        records = json.load(file)
        file.close()


item_split = '?commit=true'\
            'split=/'\
                '&f=id:/controlfields/001'\
                    '&f=title:/datafields/245/subfields/a'\
                        '&f=author:/datafields/100/subfields/a'\
                            '&f=publisher:/datafields/260/subfields/b'\
                                '&f=year:/year'\
                                    '&f=serie:/datafields/490/subfields/a'\
                                        '&f=termo_topico:/datafields/650/subfields/a'\
                                               '&f=type:/datafields/900/subfields/a'         




def index_solr(item_id, item_split=item_split):
    r = httpx.get(f'http://localhost:8000/cataloguing/item/{item_id}')
    record = r.json()
    year = record.get('controlfields').get('008')[7:11]
    if type(year) == int:
        record['year'] = year

    solr = httpx.post(
    f'http://localhost:8983/solr/acervo/update/json/docs{item_split}', json=record)

    print(solr)

   
items = [23,24,25,26,27,28,29,30,31,37]
for item_id in items:
    index_solr(item_id)
    


