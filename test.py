from src.db.init_db import session
from src.db.models import User

user_id = 7


user = session.query(User).filter_by(id = user_id).first()