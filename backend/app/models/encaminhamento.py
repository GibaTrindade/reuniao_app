from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP, Date
from sqlalchemy.sql import func
import sqlalchemy.orm as _orm
from ..configs.db import meta, Base
from .enc_reuniao import enc_reunioes

# API get from DB asking for theses models
# API pega do BD baseada nesses modelos
#enc_reunioes = Table('enc_reunioes', Base.metadata,
#    Column('enc_id', ForeignKey('encaminhamentos.id'), primary_key=True),
#    Column('reuniao_id', ForeignKey('reunioes.id'), primary_key=True)
#)


class Encaminhamento(Base):
    __tablename__ = "encaminhamentos"
    id = Column(Integer, primary_key=True, index=True)
    assunto = Column(String(200))
    tema = Column(String(200))
    observacao = Column(String(1000))
    status = Column(String(15))
    

    reunioes: list = _orm.relationship("Reuniao", secondary="enc_reunioes", back_populates="encaminhamentos")
    

