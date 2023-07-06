from .reuniao import ReuniaoBase
from .encaminhamento import EncaminhamentoBase
from typing import TYPE_CHECKING, List


class Encaminhamento(EncaminhamentoBase):
    reunioes: List[ReuniaoBase]

