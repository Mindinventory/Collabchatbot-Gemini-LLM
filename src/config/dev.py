from dotenv import load_dotenv, find_dotenv
import os
from pydantic import BaseConfig
from pathlib import Path

load_dotenv(find_dotenv())


class Settings(BaseConfig):
    DEBUG: bool = False


class DatabaseSettings(BaseConfig):
    DATABASE_USERNAME: str = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")
    SQLITE_URL: str = (
        Path(__file__).parent.parent.absolute() / "repositories" / "mind.db"
    )


class Environment(BaseConfig):
    BASE_DIR: str = Path(__file__).parent.parent.absolute()


environ = Environment()
