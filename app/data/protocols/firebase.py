from abc import ABCMeta, abstractmethod
from pydantic import BaseModel


class UploadInput(BaseModel):
    content_type: str
    blob_path: str
    file_path: str


class UploadRepository(metaclass=ABCMeta):
    Input = UploadInput

    @abstractmethod
    async def upload(self, data: Input) -> str:
        pass


class DeleteRepository(metaclass=ABCMeta):
    @abstractmethod
    async def delete(self, blob_path: str) -> None:
        pass


class DeleteBlobRepository(metaclass=ABCMeta):
    @abstractmethod
    async def delete_blob(self, blob_path: str) -> None:
        pass
