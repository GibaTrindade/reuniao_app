from pydantic import BaseModel
from typing import TYPE_CHECKING, List


class ReuniaoCreate(BaseModel):
    nome: str

    class Config:
        orm_mode = True


class ReuniaoUpdate(BaseModel):
    nome: str = None

    class Config:
        orm_mode = True


class ReuniaoBase(ReuniaoCreate):
    id: int
    nome: str








