from sqlalchemy import create_engine, MetaData, orm
from sqlalchemy.ext import declarative
from ..config import settings

user = settings.BD_USER
password = settings.BD_PASSWORD
host = settings.BD_HOST
database = settings.BD_DATABASE
port = settings.BD_PORT
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

#engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
meta = MetaData()
conn = engine.connect()
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative.declarative_base()
