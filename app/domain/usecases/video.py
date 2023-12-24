from abc import ABCMeta, abstractmethod
from pydantic import BaseModel


class UploadVideoInput(BaseModel):
    uuid: str
    file: bytes


class UploadVideo(metaclass=ABCMeta):
    Input = UploadVideoInput

    @abstractmethod
    async def upload_video(self, data: Input) -> str:
        pass


class RemoveVideoInput(BaseModel):
    user_uuid: str
    video_uuid: str


class RemoveVideo(metaclass=ABCMeta):
    Input = RemoveVideoInput

    @abstractmethod
    async def remove_video(self, data: Input) -> None:
        pass
