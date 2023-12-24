from fastapi.params import File as MediaFile
from fastapi import Request, UploadFile, File
from app.schemas.media import MediaType
from .request_file import RequestFile
from typing import Annotated


class VideoFile:
    VIDEO_FILE: MediaFile = File(
        media_type="video/*",
        description="An uploaded video file"
    )

    def __init__(self) -> None:
        self.request_file = RequestFile(MediaType.image)

    async def __call__(
        self,
        request: Request,
        video: Annotated[UploadFile, VIDEO_FILE] = None
    ):
        return await self.request_file.media(request, video)
