import httpx

term_topico = '?commit=true'\
            'split=/'\
                '&f=id:/id'\
                '&f=termo_topico:/datafields/150/subfields/a'\
                        '&f=termo_topico.ver:/datafields/450/subfields/a'\
                            '&f=termo_topico.ver_tambem:/datafields/550/subfields/a'\
                                '&f=termo_topico.vocabulario_alternativo:/datafields/750/subfields/a'

personal_name = '?commit=true'\
            'split=/'\
                '&f=id:/id'\
                '&f=personal_name:/datafields/100/subfields/a'\
                        '&f=personal_name.ver:/datafields/400/subfields/a'

corporate_name = '?commit=true'\
            'split=/'\
                '&f=id:/id'\
                '&f=corporate_name:/datafields/110/subfields/a'\
                        '&f=corporate_name.ver:/datafields/410/subfields/a'

geographic_name = '?commit=true'\
            'split=/'\
                '&f=id:/id'\
                '&f=geographic_name:/datafields/151/subfields/a'\
                        '&f=geographic_name.ver:/datafields/451/subfields/a'

def update_solr(request, authority, type):

    split = {
        100: personal_name,
        110: corporate_name,
        151: geographic_name,
        150:  term_topico}
  
    doc_solr = request.dict()
    doc_solr['id'] = authority.id

    res = httpx.post(
    f'http://localhost:8983/solr/thesaurus/update/json/docs{split[type]}', json=doc_solr)

