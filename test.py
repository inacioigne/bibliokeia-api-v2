
from src.db.init_db import session
from src.db.models import Exemplar, User, Loan
from src.schemas.users.user_schema import User_Response

user_id = 11
register = "22-0001"

loan = Loan()




user = session.query(User).filter_by(id = user_id).first()
ex = session.query(Exemplar).filter_by(number = register).first()

