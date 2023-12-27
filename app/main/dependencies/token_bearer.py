from app.main.exceptions import Unauthorized, InvalidUuid
from ...infra.auth.jwt_auth_repository import JwtRepository
from fastapi import Header, Request
from bson import ObjectId


class JwtBearer:
    BEARER = Header(
        default=None,
        alias="jwt-token-bearer",
        description="A JWT Token Bearer"
    )

    def __init__(self):
        self.__jwt_repository = JwtRepository()

    async def __call__(self, request: Request, jwt_token_bearer: str = BEARER):

        if jwt_token_bearer:
            return self.__jwt_repository.decode_token(jwt_token_bearer).subject

        authorization = request.headers.get("Authorization")

        if not authorization:
            raise Unauthorized("No bearer token provided")

        scheme, _, credentials = authorization.partition(" ")

        if not (scheme and credentials):
            raise Unauthorized("No bearer token provided")

        if scheme.lower() != "bearer":
            raise Unauthorized("Invalid authentication scheme")

        uuid = self.__jwt_repository.decode_token(credentials).subject

        if not ObjectId.is_valid(uuid):
            raise InvalidUuid("user")

        return uuid
