from sqlalchemy import (
    NVARCHAR,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Table,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.config.db import Base
from app.constants import PermissionCode

MAX_VARCHAR_LENGTH = 255
MEDIUM_VARCHAR_LENGTH = 100


class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(), default=func.now())
    modified_at = Column(DateTime(), default=func.now(), onupdate=func.now())


user_permission = Table(
    "user_permission",
    Base.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey(
            "users.id",
            name="fk_user_permission_user",
        ),
    ),
    Column(
        "permission_id",
        Integer,
        ForeignKey(
            "permissions.id",
            name="fk_user_permission_permission",
        ),
    ),
)


class User(BaseMixin, Base):
    __tablename__ = "users"
    email = Column(NVARCHAR(MEDIUM_VARCHAR_LENGTH), unique=True, nullable=False)
    hashed_password = Column(NVARCHAR(MAX_VARCHAR_LENGTH), nullable=False)
    is_superuser = Column(Boolean(), default=False)

    permissions = relationship("Permission", secondary=user_permission, backref="users")


class Permission(BaseMixin, Base):
    __tablename__ = "permissions"
    name = Column(NVARCHAR(MEDIUM_VARCHAR_LENGTH), nullable=False, unique=True)
    code = Column(Enum(PermissionCode), nullable=False)
