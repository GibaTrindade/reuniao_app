from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    is_partner: bool
    is_admin: bool
    #businesses: List[Reuniao] = []

    class Config:
        orm_mode = True

class ChangePassword(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str