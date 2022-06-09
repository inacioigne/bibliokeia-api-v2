import httpx

doc_solr = {
    'id': 2,
    "leader": "01060cz  a2200205o  4500",
    "datafields": {
        "040": {
            "indicators": {
                "Ind1": "_",
                "Ind2": "_"
            },
            "subfields": {
                "a": "BR-RjBN ",
                "b": "por"
            }
        },
        "100": {
            "indicators": {
                "Ind1": "1",
                "Ind2": "_"
            },
            "subfields": {
                "a": "Assis, Machado de, ",
                "d": "1839-1908"
            }
        },
        "400": {
            "indicators": {
                "Ind1": "1",
                "Ind2": "_"
            },
            "subfields": {
                "a": "Machado de Assis, Joaquim Maria ",
                "d": "1839-1908"
            }
        },
        "670": {
            "indicators": {
                "Ind1": "_",
                "Ind2": "_"
            },
            "subfields": {
                "a": "https://catalogue.bnf.fr/ark:/12148/cb118893083  17/03/2021 ",
                "b": "(D.)"
            }
        }
    },
    "controlfields": {
        "008": "970715   acnnnab n           a aaa      "
    }
}

""" res = httpx.post(
    f'http://localhost:8983/solr/thesarus/update/json/docs'\
        '?commit=true'\
            'split=/'\
                '&f=id:/id'\
                '&f=termo_topico:/datafields/150/subfields/a'\
                    '&f=termo_topico:/datafields/150/subfields/a'\
                        '&f=remissiva_ver:/datafields/450/subfields/a', json=doc_solr) """

x = {"delete": { "id":"f2aefc1f-d2b0-4519-b561-33c843e90056" }}
res = httpx.post(
    f'http://localhost:8983/solr/thesarus/update/json/docs'\
        '?commit=true?json.command=true', json=x)