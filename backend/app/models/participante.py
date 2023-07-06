from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.orm as _orm
from ..configs.db import Base


# API get from DB asking for theses models
# API pega do BD baseada nesses modelos
#enc_reunioes = Table('enc_reunioes', Base.metadata,
#    Column('enc_id', ForeignKey('encaminhamentos.id'), primary_key=True),
#    Column('reuniao_id', ForeignKey('reunioes.id'), primary_key=True)
#)


class Participante(Base):
    __tablename__ = "participantes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    lotacao = Column(String(50))
    matricula = Column(String(10), nullable=True)
    reuniao_id = Column(Integer, ForeignKey('reunioes.id'), nullable=True)

    reunioes = _orm.relationship("Reuniao", back_populates="participantes")
    

