from sqlalchemy import Column, String

from db_migration.db.sqlalchemy.models import base


class User(base.Base):
    __tablename__ = "users"
    id = Column("id", String(length=255), primary_key=True, comment="id")
    name = Column("name", String(length=25), comment="用户名")
    password = Column("password", String(length=255), comment="密码")
