from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy import orm
from ..configs.db import conn
from ..schemas.index import Reuniao, ReuniaoCreate, ReuniaoUpdate
from ..models.index import Reuniao as BD_Reuniao
from ..models.index import Encaminhamento as BD_Encaminhamento
from ..services import get_db, get_all_reunioes, get_reuniao_by_id, get_enc_by_id, \
     add_reuniao_a_enc, create_reuniao, update_reuniao

import json

reuniao = APIRouter()

#response_model=List[Reuniao],
@reuniao.get("/reuniao", response_model=List[Reuniao], tags=["reuniao"])#, response_model=List[Reuniao]
async def read_data(db: orm.Session=Depends(get_db)):
    db_reuniao = get_all_reunioes(db=db)
    return db_reuniao


#@reuniao.get("/reuniao/{id}", tags=["reuniao"])
#async def read_data(id: int, db: orm.Session=Depends(get_db)):
#    return get_reuniao_by_id(db=db, reuniao_id=id)


@reuniao.post("/reunioes/", response_model=Reuniao, tags=["reuniao"])
def criar_reuniao(reuniao: ReuniaoCreate, db: orm.Session = Depends(get_db)):
    bd_reuniao = create_reuniao(reuniao, db)
    return bd_reuniao

@reuniao.post("/encaminhamento/{encaminhamento_id}/adicionar_reuniao/{reuniao_id}")
def adicionar_encaminhamento(reuniao_id: int, encaminhamento_id: int, db: orm.Session = Depends(get_db)):
    reuniao: BD_Reuniao = get_reuniao_by_id(db, reuniao_id)
    encaminhamento: BD_Encaminhamento = get_enc_by_id(db, encaminhamento_id)
    
    if not reuniao or not encaminhamento:
        raise HTTPException(status_code=404, detail="Reunião ou encaminhamento não encontrado.")
    
    add_reuniao_a_enc(db, encaminhamento, reuniao)
    
    return {"message": "Reunião adicionada ao encaminhamento com sucesso."}

@reuniao.patch("/reuniao/{item_id}", response_model=Reuniao, tags=["reuniao"])
def update_item(reuniao_id: str, reuniao: ReuniaoUpdate, db: orm.Session = Depends(get_db)):
    db_reuniao = update_reuniao(db=db, reuniao_id=reuniao_id, reuniao=reuniao)
    
    return db_reuniao