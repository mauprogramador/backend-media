from datetime import datetime
from http import HTTPStatus
from bson import ObjectId


def serialize_object_id(field: ObjectId) -> str:
    return str(field)


def serialize_datetime(field: datetime) -> str:
    return field.strftime("%d-%m-%Y %H:%M:%S")


def serialize_list(field: list) -> int:
    return 0 if field is None else len(field)


def exceptions_responses(*args: int):
    content = "Exceptions: "
    for status in args:
        content += f"\n- **{status}**: {HTTPStatus(status).phrase}"
    return content
