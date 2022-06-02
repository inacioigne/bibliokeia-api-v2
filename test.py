
from src.db.init_db import session
from src.db.models import Exemplar, User, Loan, Item
from src.schemas.users.user_schema import User_Response

user_id = 1
log =  {'creator': {'id': 1, 'name': "eu" }}
register = "22-0002"

user = session.query(User).filter_by(id = user_id).first()
loan = Loan(log=log)

