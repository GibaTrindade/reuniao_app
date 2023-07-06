from sqlalchemy import Table, Column, ForeignKey
from ..configs.db import meta, Base

enc_reunioes = Table('enc_reunioes', Base.metadata,
    Column('enc_id', ForeignKey('encaminhamentos.id'), primary_key=True),
    Column('reuniao_id', ForeignKey('reunioes.id'), primary_key=True)
)
    
