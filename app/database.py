import sqlalchemy as db
from app.settings import DIRECT_DATABASE_URL

engine = db.create_engine(DIRECT_DATABASE_URL, echo=True)
conn = engine.connect()