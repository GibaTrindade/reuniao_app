from pydantic import BaseModel
from typing import TYPE_CHECKING, List, Optional
#from .reuniao import ReuniaoBase



class ParticipanteCreate(BaseModel):
    nome: str
    lotacao: str 
    matricula: str = None
    reuniao_id: Optional[int] = None

    class Config:
        orm_mode = True

class ParticipanteUpdate(BaseModel):
    nome: str = None
    lotacao: str = None
    matricula: str = None
    reuniao_id: Optional[int] = None

    class Config:
        orm_mode = True


class ParticipanteBase(ParticipanteCreate):
    id: int
    






