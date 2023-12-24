from hashlib import sha224
from time import time_ns


ENCODING = "utf-8"


def hash_uuid(uuid: str) -> str:
    return sha224(uuid.encode(ENCODING)).hexdigest()


def generate_uuid(uuid: str) -> str:
    data = f"{uuid}{time_ns()}"
    return sha224(data.encode(ENCODING)).hexdigest()
