from typing import Callable, Awaitable, Annotated
from starlette.responses import Response
from pydantic import BaseModel, constr
from fastapi import Request, Path


CALL_NEXT_RESPONSE = Callable[[Request], Awaitable[Response]]

UUID_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    strict=True,
    min_length=24,
    max_length=24,
    pattern=r"^[a-zA-Z0-9]{24}$"
)]
PATH_UUID = Annotated[UUID_VALIDATOR, Path(description="Video UUID")]

IMAGE_UPLOAD_DESCRIPTION = """
## Headers
```
Content-Type: multipart/form-data
Accept: image/*
```
"""

VIDEO_UPLOAD_DESCRIPTION = """
## Headers
```
Content-Type: multipart/form-data
Accept: video/*
```
"""


class BaseResponse(BaseModel):
    message: str
    success: bool = True


class MessageResponse(BaseResponse):
    pass
