from pydantic import BaseModel
from enum import Enum


class MediaType(Enum):
    image = "image"
    video = "video"


class MediaInput(BaseModel):
    uuid: str
    file: bytes


class RemoveVideoInput(BaseModel):
    user_uuid: str
    video_uuid: str

    @staticmethod
    def make(user_uuid: str, video_uuid: str):
        return RemoveVideoInput(
            user_uuid=user_uuid,
            video_uuid=video_uuid
        )
