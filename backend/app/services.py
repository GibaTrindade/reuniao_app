import fastapi
from fastapi import Depends, security, HTTPException
#from fastapi.encoders import jsonable_encoder
from sqlalchemy import orm
#from typing import List
#from PIL import Image
#import base64
#from io import BytesIO
import email_validator as email_check
import passlib.hash as hash
import jwt as jwt
from .config import settings
from .configs.db import SessionLocal, Base, engine
from .models.index import Participante, Encaminhamento, Reuniao  , User as User_Model
from .schemas.index import  UserCreate, User as User_Schema, EncaminhamentoCreate,\
      EncaminhamentoUpdate, ReuniaoCreate, ReuniaoUpdate, ParticipanteCreate, ParticipanteUpdate

SECRET = settings.TOKEN_SECRET

oauth2schema = security.OAuth2PasswordBearer("/token")
def create_database():
    return Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_by_id(db: orm.Session, user_id: int):
    return db.query(User_Model).filter(User_Model.id == user_id).first()

def get_all_users(db: orm.Session):
    return db.query(User_Model).all()


def get_user_by_email(db: orm.Session, email: str):
    return db.query(User_Model).filter(User_Model.email == email).first()


def get_users(db: orm.Session, skip: int = 0, limit: int = 100):
    return db.query(User_Model).offset(skip).limit(limit).all()


async def create_user(db: orm.Session, user: UserCreate):
    try:
        valid = email_check.validate_email(email=user.email)
        email = valid.email
    except email_check.EmailNotValidError:
        raise fastapi.HTTPException(status_code=404, detail="Please enter a valid email!")


    hashed_password = hash.bcrypt.hash(user.password)
    db_user = User_Model(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: orm.Session, user_id: int, user: UserCreate):
    try:
        valid = email_check.validate_email(email=user.email)
        email = valid.email
    except email_check.EmailNotValidError:
        raise fastapi.HTTPException(status_code=404, detail="Please enter a valid email!")

    hashed_password = hash.bcrypt.hash(user.password)
    db_user = get_user_by_id(db=db, user_id=user_id)
    db_user.email = user.email
    db_user.hashed_password = hashed_password
    db.commit()
    db.refresh(db_user)
    return db_user

async def create_token(user: User_Model):
    user_schema_obj = User_Schema.from_orm(user)
    user_dict = user_schema_obj.dict()
    token = jwt.encode(user_dict, SECRET)

    return dict(access_token=token, token_type="bearer")

def authenticate_user(email: str, password: str, db: orm.Session):
    user_token = get_user_by_email(email=email, db=db)

    if not user_token:
        return False

    if not user_token.verify_password(password=password):
        return False

    return user_token


async def get_current_user(db: orm.Session = Depends(get_db), token: str = Depends(oauth2schema)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        user = db.query(User_Model).get(payload["id"])

    except:
        raise HTTPException(
            status_code=401, detail="Invalid Email or Password"
        )
    return User_Schema.from_orm(user)


def get_all_encs(db: orm.Session):
    return db.query(Encaminhamento).all()

def get_enc_by_id(db: orm.Session, enc_id: int):
    return db.query(Encaminhamento).filter(Encaminhamento.id == enc_id).first()

def create_enc(encaminhamento: EncaminhamentoCreate, db: orm.Session):
    enc_dict = encaminhamento.dict()
    db_encaminhamento = Encaminhamento(**enc_dict)
                                        
    db.add(db_encaminhamento)
    db.commit()
    db.refresh(db_encaminhamento)
    return db_encaminhamento

def update_enc(db: orm.Session, enc_id: int, enc: EncaminhamentoUpdate):
    db_enc = get_enc_by_id(db=db, enc_id=enc_id)
    if not db_enc:
        raise HTTPException(status_code=404, detail="Encaminhamento não encontrado!")
    enc_data = enc.dict(exclude_unset=True)
    for key, value in enc_data.items():
        setattr(db_enc, key, value)
    db.add(db_enc)
    db.commit()
    db.refresh(db_enc)
    return db_enc
    
    
    #db_enc = get_enc_by_id(db=db, enc_id=enc_id)
    #update_item_encoded = jsonable_encoder(enc)
    #db_enc = update_item_encoded
    #db_enc = Encaminhamento(**enc.dict())
    #db_enc.assunto = enc.assunto
    #db_enc.tema = enc.tema
    #db_enc.observacao = enc.observacao
    #db_enc.status = enc.status

    #db.add(db_enc)
    #db.commit()
    #db.refresh(db_enc)

    #return db_enc


def get_all_reunioes(db: orm.Session):
    return db.query(Reuniao).all()

def get_reuniao_by_id(db: orm.Session, reuniao_id: int):
    return db.query(Reuniao).filter(Reuniao.id == reuniao_id).first()

def create_reuniao(reuniao: ReuniaoCreate, db: orm.Session):
    reuniao_dict = reuniao.dict()
    bd_reuniao = Reuniao(**reuniao_dict)
    db.add(bd_reuniao)
    db.commit()
    db.refresh(bd_reuniao)
    return bd_reuniao

def update_reuniao(db: orm.Session, reuniao_id: int, reuniao: ReuniaoUpdate ):
    db_reuniao = get_reuniao_by_id(db=db, reuniao_id=reuniao_id)
    if not db_reuniao:
        raise HTTPException(status_code=404, detail="Reunião não encontrada!")
    reuniao_data = reuniao.dict(exclude_unset=True)
    for key, value in reuniao_data.items():
        setattr(db_reuniao, key, value)
    db.add(db_reuniao)
    db.commit()
    db.refresh(db_reuniao)
    return db_reuniao


def add_reuniao_a_enc(db: orm.Session, encaminhamento: Encaminhamento, reuniao: Reuniao):
    encaminhamento.reunioes.append(reuniao)
    
    db.commit()

def add_enc_a_reuniao(db: orm.Session, encaminhamento: Encaminhamento, reuniao: Reuniao):
    reuniao.encaminhamentos.append(encaminhamento)
    
    db.commit()

def update_enc_da_reuniao(db: orm.Session, encaminhamento_excluir: Encaminhamento,  
                          encaminhamento_incluir: Encaminhamento, reuniao: Reuniao):

    reuniao.encaminhamentos.remove(encaminhamento_excluir)
    reuniao.encaminhamentos.append(encaminhamento_incluir)
    db.add(reuniao)
    db.commit()
    db.refresh(reuniao)

def get_all_parts(db: orm.Session):
    return db.query(Participante).all()

def get_participante_by_id(db: orm.Session, participante_id: int):
    return db.query(Participante).filter(Participante.id == participante_id).first()

def create_participante(participante: ParticipanteCreate, db: orm.Session):
    part_dict = participante.dict()
    bd_part = Participante(**part_dict)
    db.add(bd_part)
    db.commit()
    db.refresh(bd_part)
    return bd_part

def update_participante(db: orm.Session, participante_id: int, participante: ParticipanteUpdate ):
    db_participante = get_participante_by_id(db=db, participante_id=participante_id)
    if not db_participante:
        raise HTTPException(status_code=404, detail="Participante não encontrado!")
    participante_data = participante.dict(exclude_unset=True)
    for key, value in participante_data.items():
        setattr(db_participante, key, value)
    db.add(db_participante)
    db.commit()
    db.refresh(db_participante)
    return db_participante


def add_participante_a_reuniao(db: orm.Session, participante: Participante, reuniao: Reuniao):
    reuniao.participantes.append(participante)
    db.add(reuniao)
    db.commit()
    db.refresh(reuniao)