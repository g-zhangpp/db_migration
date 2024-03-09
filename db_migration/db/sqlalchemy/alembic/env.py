from logging import config as log_config

from alembic import context

from db_migration import db
from db_migration.db.sqlalchemy.models import base
import db_migration.db.sqlalchemy.models

config = context.config
log_config.fileConfig(config.config_file_name)


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    :param target_metadata: Model's metadata used for autogenerate support.
    :param version_table: Override the default version table for alembic.
    """
    with db.session_for_write() as session:
        engine = session.get_bind()
        with engine.connect() as connection:
            context.configure(connection=connection,
                              target_metadata=base.Base.metadata)
            with context.begin_transaction():
                context.run_migrations()


run_migrations_online()

