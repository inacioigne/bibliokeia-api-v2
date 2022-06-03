
from src.db.init_db import session
from src.db.models import Exemplar, User, Loan, Item
from src.schemas.users.user_schema import User_Response
from datetime import datetime

user_id = 1
log =  {'creator': {'id': 1, 'name': "eu" }}
register = "22-0002"

loans = session.query(Loan).filter_by(user_id = 1).filter_by(status = "Emprestado").all()

q = session.query(Exemplar).filter_by(number = '22-0001') \
.join(Loan).filter_by(status = "Emprestado").first()

loan = session.query(Loan).filter_by(status = "Emprestado") \
.join(Loan.exemplar).filter_by(number = '22-0001').all()


