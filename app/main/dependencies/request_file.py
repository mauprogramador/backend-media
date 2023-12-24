from app.main.exceptions import UnsupportedMediaType, RequiredRequestFile
from fastapi import Request, UploadFile
from app.schemas.media import MediaType


class RequestFile:
    CONTENT_TYPE_HEADER = "Content-Type"
    CONTENT_TYPE_VALUE = "multipart/form-data"
    ACCEPT_HEADER = "Accept"
    ORIGIN = "origin"

    def __init__(self, media_type: MediaType):
        self.accept_value = f"{media_type.value}/*"

    async def media(self, request: Request, media: UploadFile | None):
        content_type = request.headers.get(self.CONTENT_TYPE_HEADER)

        if not content_type or not content_type.count(self.CONTENT_TYPE_VALUE):
            raise UnsupportedMediaType(self.CONTENT_TYPE_HEADER)

        if request.base_url == f"{request.headers.get(self.ORIGIN)}/":
            accept = self.accept_value
        else:
            accept = request.headers.get(self.ACCEPT_HEADER)

        if not accept or not accept.count(self.accept_value):
            raise UnsupportedMediaType(self.ACCEPT_HEADER)

        if not media:
            raise RequiredRequestFile()

        return media
