from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy import orm
from ..configs.db import conn
from ..schemas.index import Aircraft
from ..services import get_db, get_all_aircrafts

partner = APIRouter()

@partner.get("/partner/{id}")
async def read_data(db: orm.Session=Depends(get_db)):
    db_aircrafts = get_all_aircrafts(db=db)
    return db_aircrafts