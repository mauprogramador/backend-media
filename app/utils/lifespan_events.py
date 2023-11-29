from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.main.config import Lifespan
from app.infra.mongo import MongoConnection
from .logger import Logger
# import webbrowser


@asynccontextmanager
async def lifespan(_: FastAPI):
    if not all(Lifespan.envs):
        message = "Environment Variables must be specified"
        Logger.error(message)
        raise ValueError(message)
    with MongoConnection() as _:
        pass
    # webbrowser.get(Lifespan.browser).open(Lifespan.swagger)
    Logger.info("\033[33mConnected to the MongoDB database\033[m")
    yield
