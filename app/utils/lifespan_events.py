from app.infra.firebase import FirebaseService
from app.infra.mongo import MongoConnection
from contextlib import asynccontextmanager
from app.main.config import ENVS
from fastapi import FastAPI
from .logger import Logger


@asynccontextmanager
async def lifespan(_: FastAPI):
    if not all(ENVS):
        message = "Environment Variables must be specified"
        Logger.error(message)
        raise ValueError(message)
    with MongoConnection() as _:
        pass
    Logger.info("\033[33mConnected to the MongoDB database\033[m")
    FirebaseService.load_bucket()
    Logger.info("\033[33mConnected to the Firebase service\033[m")
    yield
