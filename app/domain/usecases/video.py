from abc import ABCMeta, abstractmethod


class UploadVideo(metaclass=ABCMeta):
    @abstractmethod
    async def upload(self) -> str:
        pass


class DeleteVideo(metaclass=ABCMeta):
    @abstractmethod
    async def delete(self, url: str) -> None:
        pass
