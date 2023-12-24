from app.main.exceptions import ExceptionHandler
from app.utils.lifespan_events import lifespan
from app.main.middlewares import TraceControl
from app.utils.logger import Logger
from app.main.config import FASTAPI
from app.main.routes import ROUTES
from fastapi import FastAPI


app = FastAPI(
    **FASTAPI,
    lifespan=lifespan,
    exception_handlers=ExceptionHandler.handlers()
)

app.add_middleware(TraceControl)


for router in ROUTES:
    app.include_router(router)


Logger.info("\033[33mSnapcut Backend Media Service was Initialized 🚀\033[m")
