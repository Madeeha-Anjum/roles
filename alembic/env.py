from calendar import c
import sqlalchemy as db

from alembic import context


from app.models import Base
from app import DIRECT_DATABASE_URL, settings

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
config.set_main_option("sqlalchemy.url", DIRECT_DATABASE_URL)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
# if config.config_file_name is not None:
# fileConfig(config.config_file_name)


# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = [Base.metadata]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = db.engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=db.pool.NullPool,
    )
    
    with connectable.connect() as connection:
        print("🔹 Connected to the database!")
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema="public",  # Ensure Alembic version table stays in public
            schema_translate_map={None: settings.SCHEMA_NAME},  # Set schema for tables
        )
        
        query = f"CREATE SCHEMA IF NOT EXISTS {settings.SCHEMA_NAME};"
        connection.execute(db.text(query))
        
        connection.execute(db.text(f"SET search_path TO {settings.SCHEMA_NAME};"))
        x = connection.execute(db.text(f"SELECT current_schema();"))
        print(f"🔹 Current schema: {x.first()[0]}")
        with context.begin_transaction():
            print("🔹 Running Alembic migrations now...")
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
