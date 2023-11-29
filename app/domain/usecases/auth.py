from abc import ABCMeta, abstractmethod


class GetToken(metaclass=ABCMeta):
    @abstractmethod
    async def get_token(self, uuid: str) -> Output:
        pass
