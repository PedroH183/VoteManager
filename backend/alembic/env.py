import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine

from alembic import context
from app.infra.db.database import Base

# carrega o arquivo alembic.ini
config = context.config
fileConfig(config.config_file_name)

# importa aqui seus models, para registrar metadata
# e permitir autogenerate encontrar todas as tabelas
from app.infra.db.models.topic_model import Topic
from app.infra.db.models.session_model import Session
from app.infra.db.models.vote_model import Vote

target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode (sem conexão)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    """Run migrations in 'online' async mode."""
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        # associa a conexão async ao contexto sync do Alembic
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

def do_run_migrations(connection: Connection):
    """Callback síncrono para rodar as migrations."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,  # opcional: força diff de tipos
    )
    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    # Alembic espera uma chamada síncrona, então usamos asyncio.run
    asyncio.run(run_migrations_online())
