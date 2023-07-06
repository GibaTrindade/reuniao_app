from .reuniao import ReuniaoBase
from .participante import ParticipanteBase
from typing import TYPE_CHECKING, List, Optional


class Participante(ParticipanteBase):
    reunioes: Optional[ReuniaoBase]
