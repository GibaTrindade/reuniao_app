#from pydantic import BaseSettings
import os
from dotenv import load_dotenv, dotenv_values

from pathlib import Path

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))


class Settings:
    SERVER_HOST: str = os.getenv("SERVER_HOST")
    BD_HOST: str = os.getenv("BD_HOST")
    BD_PASSWORD: str = os.getenv("BD_PASSWORD")
    BD_DATABASE: str = os.getenv("BD_DATABASE")
    BD_USER: str = os.getenv("BD_USER")
    BD_PORT: str = os.getenv("BD_PORT")
    TOKEN_SECRET: str = os.getenv("TOKEN_SECRET")
    TEST: str = os.getenv("TEST")


settings = Settings()