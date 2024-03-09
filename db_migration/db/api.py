from oslo_config import cfg
from oslo_db import api as db_api

_BACKEND_MAPPING = {'sqlalchemy': 'db_migration.db.sqlalchemy.api'}
IMPL = db_api.DBAPI.from_config(cfg.CONF,
                                backend_mapping=_BACKEND_MAPPING,
                                lazy=True)


def get_instance():
    """Return a DB API instance."""
    return IMPL
