from pydantic import BaseModel, ConfigDict
from abc import ABCMeta, abstractmethod
from PIL.Image import Image


class ImageProcessingRepository(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, file: bytes) -> Image:
        pass


class UploadImageInput(BaseModel):
    image: Image
    uuid: str

    model_config = ConfigDict(arbitrary_types_allowed=True)


class DeleteImageRepository(metaclass=ABCMeta):
    @abstractmethod
    def delete_image(self, blob_path: str) -> None:
        pass


class InsertPhotoInput(BaseModel):
    uuid: str
    url: str
    blob: str


class UploadImageRepository(metaclass=ABCMeta):
    Input = UploadImageInput
    Output = InsertPhotoInput

    @abstractmethod
    def upload_image(self, data: Input) -> Output:
        pass


class InsertPhotoRepository(metaclass=ABCMeta):
    Input = InsertPhotoInput

    @abstractmethod
    async def insert_photo(self, data: Input) -> None:
        pass


class RemovePhotoRepository(metaclass=ABCMeta):
    @abstractmethod
    async def remove_photo(self, uuid: str) -> str:
        pass
