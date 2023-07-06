from pydantic import BaseModel
from typing import TYPE_CHECKING, List
from enum import Enum

class Status(str, Enum):
    INICIADO = 'INICIADO'
    FINALIZADO = 'FINALIZADO'
    ATRASADO = 'ATRASADO'
    CANCELADO = 'CANCELADO'


class EncaminhamentoCreate(BaseModel):
    assunto: str
    tema: str
    observacao: str
    status: Status = None
    
    class Config:
        orm_mode = True

class EncaminhamentoUpdate(BaseModel):
    assunto: str = None
    tema: str = None
    observacao: str = None
    status: Status = None
    
    class Config:
        orm_mode = True


class EncaminhamentoBase(EncaminhamentoCreate):
    id: int








