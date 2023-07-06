from sqlalchemy import TIMESTAMP, Column, Integer, String, ForeignKey, Date
from sqlalchemy.sql import func
from ..configs.db import meta, Base
import sqlalchemy.orm as _orm

class Reuniao(Base):
    __tablename__ = "reunioes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200))
    #data_reuniao = Column(Date)
    #createdAt = Column(TIMESTAMP(timezone=True),
    #                   nullable=False, server_default=func.now())

    encaminhamentos: list = _orm.relationship("Encaminhamento", secondary="enc_reunioes", back_populates="reunioes")
    participantes: list = _orm.relationship("Participante", back_populates="reunioes")
    
