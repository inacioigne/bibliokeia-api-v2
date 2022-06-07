
from src.db.init_db import session
from src.db.models import Exemplar, User, Loan, Item, Authority, Access_Points
from src.schemas.users.user_schema import User_Response
from datetime import datetime


au = session.query(Authority).filter_by(marc['datafields']['150']['subfields']['a'] == 'Azul')
