from typing import TYPE_CHECKING, List
from .reuniao import ReuniaoBase
from .encaminhamento import EncaminhamentoBase
from .participante import ParticipanteBase
#from .enc_schema import Encaminhamento
#from .encaminhamento import EncaminhamentoBase


class Reuniao(ReuniaoBase):
    encaminhamentos: List[EncaminhamentoBase]
    participantes: List[ParticipanteBase]
