from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

# import all models before calling SQLModel.metadata.create_all()
from app.models import *

# ---------- 1. DATABASE URL ----------
engine = create_engine(
    settings.DIRECT_DATABASE_URL,
    echo=False,  # set True if you want SQL logs
)

# ---------- 2. CREATE TABLES ----------
def initialize_orm() -> None:
    SQLModel.metadata.create_all(engine)

# ---------- 3. SESSION DEPENDENCY ----------
def get_session():
    with Session(engine) as session:
        yield session
