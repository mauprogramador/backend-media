from app.domain.models import TokenModelOut
from abc import ABCMeta, abstractmethod


class CheckUserPasswordRepository(metaclass=ABCMeta):
    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        pass


class DecodeTokenRepository(metaclass=ABCMeta):
    Output = TokenModelOut

    @abstractmethod
    def decode_token(self, token: str) -> Output:
        pass
