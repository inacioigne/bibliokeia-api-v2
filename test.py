
from src.db.init_db import session
from src.db.models import Exemplar, User, Loan, Item, Authority, Access_Points
from src.schemas.users.user_schema import User_Response
from datetime import datetime
from src.schemas.items.item import Marc_Bibliographic
import httpx

a = {
    "leader": "####az###22#####n##450",
    "controlfields": {
        "003": "BR-MnINPA",
        "005": "20220606153024.0",
        "008": "220606#a||aaa##000#00por##"
    },
    "datafields": {
        "150": {
            "indicators": {
                "Ind1": "#",
                "Ind2": "#"
            },
            "subfields": {
                "a": "Tambaqui (Peixe)"
            }
        },
        "450": [
            {
                "indicators": {
                    "Ind1": "#",
                    "Ind2": "#"
                },
                "subfields": {
                    "a": "Blackfin"
                }
            },
            {
                "indicators": {
                    "Ind1": "#",
                    "Ind2": "#"
                },
                "subfields": {
                    "a": "Cachama"
                }
            },
            {
                "indicators": {
                    "Ind1": "#",
                    "Ind2": "#"
                },
                "subfields": {
                    "a": "Colossoma macropomum"
                }
            },
            {
                "indicators": {
                    "Ind1": "#",
                    "Ind2": "#"
                },
                "subfields": {
                    "a": "Colossoma nigripinne"
                }
            },
            {
                "indicators": {
                    "Ind1": "#",
                    "Ind2": "#"
                },
                "subfields": {
                    "a": "Colossoma oculus"
                }
            }
        ],
        "670": {
            "indicators": {
                "Ind1": "#",
                "Ind2": "#"
            },
            "subfields": {
                "a": "LCSH"
            }
        },
        "750": {
            "indicators": {
                "Ind1": "#",
                "Ind2": "0"
            },
            "subfields": {
                "a": "Tambaqui"
            }
        }
    }
}


request = Marc_Bibliographic(**a)

authority = session.query(Authority).filter_by(id = 7).first()



doc_solr = {
        'id': authority.id,
        'type': authority.type,
        'leader': request.leader,
    }

request.controlfields

f'http://localhost:8983/solr/authority/update/json/docs'\
    '?commit=true'\
        'split=/'\
            '&f=leader:/leader'\
                '&f=003:/controlfields/003'\
                    '&f=150:/datafields/150/subfields/a'\
                        '&f=450:/datafields/450/subfields/a'\
                            '&f=670:/datafields/670/subfields/a'\
                                '&f=750:/datafields/750/subfields/a'
controlfields = ''
for i in request.controlfields.keys():
    controlfields = controlfields+f'&f={i}:/controlfields/{i}'
    