from abc import ABCMeta, abstractmethod
from pydantic import BaseModel


class UploadPhotoInput(BaseModel):
    uuid: str
    file: bytes


class UploadPhoto(metaclass=ABCMeta):
    Input = UploadPhotoInput

    @abstractmethod
    async def upload_photo(self, data: Input) -> None:
        pass


class RemovePhoto(metaclass=ABCMeta):
    @abstractmethod
    async def remove_photo(self, uuid: str) -> None:
        pass
