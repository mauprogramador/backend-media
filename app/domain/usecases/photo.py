from abc import ABCMeta, abstractmethod


class UploadPhoto(metaclass=ABCMeta):
    @abstractmethod
    async def upload(self, data: bytes) -> str:
        pass


class ReplacePhoto(metaclass=ABCMeta):
    @abstractmethod
    async def replace(self, url: str, data: bytes) -> str:
        pass


class DeletePhoto(metaclass=ABCMeta):
    @abstractmethod
    async def delete(self, url: str) -> None:
        pass
