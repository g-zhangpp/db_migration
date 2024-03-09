import threading

from oslo_db.sqlalchemy import enginefacade

_CONTEXT = threading.local()
_FACADE = None


def _create_facade_lazily():
    global _FACADE
    if _FACADE is None:
        ctx = enginefacade.transaction_context()
        ctx.configure(sqlite_fk=True)
        _FACADE = ctx
    return _FACADE


def session_for_read():
    return _create_facade_lazily().reader.using(_CONTEXT)


def session_for_write():
    return _create_facade_lazily().writer.using(_CONTEXT)
