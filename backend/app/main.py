from typing import Union
import json
from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from .routes.index import enc, reuniao, user, participante

from pydantic import BaseModel

from .config import settings


app = FastAPI()

app.include_router(user)
app.include_router(enc)
app.include_router(reuniao)
app.include_router(participante)


origins = [
    "http://localhost:3000",
    "localhost:3000",
    "127.0.0.1:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/api")
def read_root():
    return {"message": "Hello World"}




