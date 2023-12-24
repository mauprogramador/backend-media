from pydantic import BaseModel, ConfigDict
from abc import ABCMeta, abstractmethod


class VideoProcessingRepository(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, file: bytes) -> bytes:
        pass


class UploadVideoInput(BaseModel):
    video: bytes
    uuid: str

    model_config = ConfigDict(arbitrary_types_allowed=True)


class DeleteVideoRepository(metaclass=ABCMeta):
    @abstractmethod
    def delete_video(self, blob_path: str) -> None:
        pass


class InsertVideoInput(BaseModel):
    user_uuid: str
    video_uuid: str
    url: str
    blob: str


class UploadVideoRepository(metaclass=ABCMeta):
    Input = UploadVideoInput
    Output = InsertVideoInput

    @abstractmethod
    def upload_video(self, data: Input) -> Output:
        pass


class InsertVideoRepository(metaclass=ABCMeta):
    Input = InsertVideoInput

    @abstractmethod
    async def insert_video(self, data: Input) -> None:
        pass


class RemoveVideoInput(BaseModel):
    user_uuid: str
    video_uuid: str


class RemoveVideoRepository(metaclass=ABCMeta):
    Input = RemoveVideoInput

    @abstractmethod
    async def remove_video(self, uuid: Input) -> str:
        pass
