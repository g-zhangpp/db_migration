import os

from db_migration.db.sqlalchemy import migration

ALEMBIC_REPO = os.path.join(os.path.dirname(__file__), 'sqlalchemy/alembic')


def upgrade(revision):
    config = migration.load_alembic_config(ALEMBIC_REPO)
    return migration.upgrade(config, revision)


def version():
    config = migration.load_alembic_config(ALEMBIC_REPO)
    return migration.version(config)


def revision(message, autogenerate):
    config = migration.load_alembic_config(ALEMBIC_REPO)
    return migration.revision(config, message, autogenerate)


def stamp(revision):
    config = migration.load_alembic_config(ALEMBIC_REPO)
    return migration.stamp(config, revision)
