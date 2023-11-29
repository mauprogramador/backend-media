from app.data.protocols import (
    CheckUserPasswordRepository,
    DecodeTokenRepository
)
from app.main.config import JWT
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from app.main.exceptions import InternalError, Unauthorized
from app.domain.models import TokenModelOut


class JwtRepository(
    CheckUserPasswordRepository,
    DecodeTokenRepository
):
    def __init__(self, expire: int = None) -> None:
        self.__expire = JWT.expire if not expire else expire
        self.__crypt_context = CryptContext(schemes=[JWT.scheme], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.__crypt_context.verify(plain_password, hashed_password)

    def decode_token(self, token: str) -> DecodeTokenRepository.Output:
        try:
            decoder = jwt.decode(token, JWT.secret, algorithms=JWT.algorithm)
            model_out = TokenModelOut(**decoder)
            hex_subject = model_out.subject.removeprefix("uuid:")
            model_out.subject = bytes.fromhex(hex_subject).decode("utf-8")
            return model_out
        except ExpiredSignatureError:
            raise Unauthorized("Expired JWT token")
        except JWTError:
            raise Unauthorized("Invalid JWT token")
