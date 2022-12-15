from datetime import datetime

from pydantic import BaseModel, EmailStr


class BaseMixinSchema(BaseModel):
    id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True


class PermissionBaseSchema(BaseModel):
    code: int
    name: int


class PermissionUpdateSchema(BaseModel):
    code: int | None
    name: int | None


class PermissionSchema(PermissionBaseSchema, BaseMixinSchema):
    pass


class UserBaseSchema(BaseModel):
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema, BaseMixinSchema):
    pass


class UserDetail(UserBaseSchema, BaseMixinSchema):
    permissions: list[PermissionSchema] | None
