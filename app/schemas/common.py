from pydantic import BaseModel
from typing import Callable, Awaitable
from starlette.responses import Response
from fastapi import Request


CALL_NEXT_RESPONSE = Callable[[Request], Awaitable[Response]]


class BaseResponse(BaseModel):
    message: str
    success: bool = True


class MessageResponse(BaseResponse):
    pass
