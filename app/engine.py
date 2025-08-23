import sqlalchemy as db
from app import settings
from app.settings import DIRECT_DATABASE_URL
from sqlalchemy.orm import sessionmaker

engine = db.create_engine(DIRECT_DATABASE_URL, echo=True)

schema_engine = engine.connect().execution_options(
    schema_translate_map={None: settings.SCHEMA_NAME}
)
# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=(schema_engine) )


#  Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




def get_session():
    """Provide a transactional scope around a series of operations.
    Source: https://docs.sqlalchemy.org/en/20/core/connections.html#translation-of-schema-names
    """
    #  TODO MOVE UP
    # All tables with a schema of None would instead render the schema as "roles"
    # Else the schema would be None and they would be rendered as "public"
    schema_engine = engine.connect().execution_options(
        schema_translate_map={None: settings.SCHEMA_NAME}
    )

    with schema_engine.begin() as conn:
        yield conn
    
    # pass the engine to the Session
    # try:
    #     db = Session(autocommit=False, autoflush=False, bind=schema_engine)
    #     yield db
    # finally:
    #     db.close()
     