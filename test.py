from src.db.init_db import session
from src.db.models import User
from src.schemas.users.user_schema import User_Response

user_id = 4


user = session.query(User).filter_by(id = user_id).first()

user_response = user.__dict__