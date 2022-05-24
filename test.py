from src.db.init_db import session
from src.db.models import Item, Exemplar


ex = session.query(Exemplar).order_by(Exemplar.id.desc()).first()