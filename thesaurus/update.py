import json
import httpx
from parser import parser_authority

parser_authority()

with open('thesaurus/termo_topico.json') as file_json:
    data = json.load(file_json)
    data['id'] = 3
    file_json.close()

split = '?commit=true'\
            'split=/'\
                '&f=id:/id'\
                '&f=termo_topico:/datafields/150/subfields/a'\
                    '&f=termo_topico:/datafields/150/subfields/a'\
                        '&f=termo_topico.ver:/datafields/450/subfields/a'\
                            '&f=termo_topico.ver_tambem:/datafields/550/subfields/a'

res = httpx.post(
    f'http://localhost:8983/solr/thesaurus/update/json/docs{split}', json=data)