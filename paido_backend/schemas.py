from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class BaseUserSchema(BaseModel):
    username: str
    email: EmailStr


class UserSchema(BaseUserSchema):
    password: str


class UserDB(UserSchema):
    id: int


class UserPublic(BaseUserSchema):
    id: int
