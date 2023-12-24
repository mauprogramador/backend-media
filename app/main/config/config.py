from app.main.exceptions import BaseExceptionResponse
from . import env


BASE_EXCEPTION_RESPONSE = {
    422: {
        "model": BaseExceptionResponse,
        "description": "Base Exception Response"
    }
}

FASTAPI = dict(
    title=env.APP_TITLE,
    summary=env.APP_SUMMARY,
    description=env.APP_DESCRIPTION,
    version=env.APP_VERSION,
    docs_url="/",
    responses=BASE_EXCEPTION_RESPONSE
)


ENVS = [
    env.MONGODB_URI,
    env.DATABASE,
    env.COLLECTION,
    env.SECRET_KEY,
    env.FIREBASE_BUCKET,
]

if env.MONGODB_URI is not None and env.MONGODB_URI.count("<password>"):
    ENVS.append(env.PASSWORD)


class JWT:
    secret = env.SECRET_KEY
    algorithm = env.ALGORITHM
    expire = env.EXPIRE_ACCESS_TOKEN_TIME
    scheme = env.CRYPTO_SCHEME
