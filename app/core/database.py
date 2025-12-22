from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

# import all models before calling SQLModel.metadata.create_all()
from app.models import *

engine = create_engine(
    settings.DIRECT_DATABASE_URL,
    echo=False,  # set True if you want SQL logs
)

def get_session():
    with Session(engine) as session:
        yield session
