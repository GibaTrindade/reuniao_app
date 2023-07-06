from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy import orm
from ..services import get_db, get_all_parts, create_participante, update_participante, add_participante_a_reuniao
from ..schemas.index import Participante, ParticipanteCreate, ParticipanteUpdate , ParticipanteBase
from ..models.index import Participante as BD_Participante, Reuniao as BD_Reuniao

participante = APIRouter()


@participante.get("/participantes/", response_model=List[Participante], tags=["participante"]) #response_model=List[Participante],
async def read_data(db: orm.Session=Depends(get_db)):
    part_list = get_all_parts(db=db)

    return part_list

@participante.post("/participante/", response_model=Participante,  tags=["participante"]) #response_model=Participante,
def criar_participante(participante: ParticipanteCreate, db: orm.Session = Depends(get_db)):
    db_participante: ParticipanteCreate = create_participante(participante, db)
    return db_participante

@participante.patch("/participante/{item_id}", response_model=Participante, tags=["participante"])
def update_item(participante_id: str, participante: ParticipanteUpdate, db: orm.Session = Depends(get_db)):
    db_participante = update_participante(db=db, participante_id=participante_id, participante=participante)
    
    return db_participante


@participante.post("/reunioes/{reuniao_id}/adicionar_participante/{participante_id}")
def adicionar_participante(reuniao_id: int, participante_id: int, db: orm.Session = Depends(get_db)):
    reuniao: BD_Reuniao = db.query(BD_Reuniao).filter(BD_Reuniao.id == reuniao_id).first()
    participante = db.query(BD_Participante).filter(BD_Participante.id == participante_id).first()

    if not reuniao or not participante:
        raise HTTPException(status_code=404, detail="Reunião ou participante não encontrados.")
    
    add_participante_a_reuniao(db, participante, reuniao)

    return {"message": "Participante adicionado à reunião com sucesso."}
