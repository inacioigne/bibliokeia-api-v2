
from src.db.init_db import session
from src.db.models import Exemplar, User, Loan, Item
from src.schemas.users.user_schema import User_Response





item = session.query(Item).first()