from app.main.exceptions import BaseExceptionResponse
from . import env


FASTAPI = dict(
    title=env.APP_TITLE,
    summary=env.APP_SUMMARY,
    description=env.APP_DESCRIPTION,
    version=env.APP_VERSION,
    docs_url="/",
    responses={422: {
        "model": BaseExceptionResponse,
        "description": "Base Exception Response"
    }}
)

ALLOW_ORIGINS = [
    "http://127.0.0.1:8000/docs"
]

ORIGIN = dict(
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


class Server:
    app = FASTAPI
    origin = ORIGIN


class Lifespan:
    envs = ENVS
    mongo_uri = env.MONGODB_URI
    browser = env.BROWSER
    swagger = env.SWAGGER


class JWT:
    secret = env.SECRET_KEY
    algorithm = env.ALGORITHM
    expire = env.EXPIRE_ACCESS_TOKEN_TIME
    scheme = env.CRYPTO_SCHEME
