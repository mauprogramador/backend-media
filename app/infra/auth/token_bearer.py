from app.main.exceptions import Unauthorized
from .jwt_auth_repository import JwtRepository
from fastapi import Header, Request
from fastapi.security import OAuth2
from typing import Any, cast


class JwtBearer:
    BEARER = Header(
        default=None,
        alias="jwt-token-bearer",
        description="A JWT Token Bearer"
    )

    def __init__(self):
        self.__jwt_repository = JwtRepository()
        # super().__init__()

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

        return self.__jwt_repository.decode_token(credentials).subject
