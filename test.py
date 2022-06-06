
from src.db.init_db import session
from src.db.models import Exemplar, User, Loan, Item, Authority, Access_Points
from src.schemas.users.user_schema import User_Response
from datetime import datetime

# user_id = 1
# log =  {'creator': {'id': 1, 'name': "eu" }}

# marc = {
#     "leader": "####az###22#####n##450",
#     "controlfields": {
#         "003": "BR-MnINPA",
#         "005": "20220606153024.0",
#         "008": "220606#a||aaa##000#00por##"
#     },
#     "datafields": {
#         "150": {
#             "indicators": {
#                 "Ind1": "#",
#                 "Ind2": "#"
#             },
#             "subfields": {
#                 "a": "Tambaqui (Peixe)"
#             }
#         },
#         "450": [
#             {
#                 "indicators": {
#                     "Ind1": "#",
#                     "Ind2": "#"
#                 },
#                 "subfields": {
#                     "a": "Blackfin"
#                 }
#             },
#             {
#                 "indicators": {
#                     "Ind1": "#",
#                     "Ind2": "#"
#                 },
#                 "subfields": {
#                     "a": "Cachama"
#                 }
#             },
#             {
#                 "indicators": {
#                     "Ind1": "#",
#                     "Ind2": "#"
#                 },
#                 "subfields": {
#                     "a": "Colossoma macropomum"
#                 }
#             },
#             {
#                 "indicators": {
#                     "Ind1": "#",
#                     "Ind2": "#"
#                 },
#                 "subfields": {
#                     "a": "Colossoma nigripinne"
#                 }
#             },
#             {
#                 "indicators": {
#                     "Ind1": "#",
#                     "Ind2": "#"
#                 },
#                 "subfields": {
#                     "a": "Colossoma oculus"
#                 }
#             }
#         ],
#         "670": {
#             "indicators": {
#                 "Ind1": "#",
#                 "Ind2": "#"
#             },
#             "subfields": {
#                 "a": "LCSH"
#             }
#         },
#         "750": {
#             "indicators": {
#                 "Ind1": "#",
#                 "Ind2": "0"
#             },
#             "subfields": {
#                 "a": "Tambaqui"
#             }
#         }
#     }
# }


# auth = Authority(
#     name = "Tambaqui",
#     marc = marc,
#     type = "Termo Tópico",
#     log = log
# )

# assuntos = Item_Subject(relation = "Termo Tópico")



# session.add(auth)
#session.commit()

item = session.query(Item).first()
