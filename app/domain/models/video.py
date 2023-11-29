from pydantic import BaseModel
from app.schemas.common import DATETIME


class VideoModelOut(BaseModel):
    url: str
    uuid: str | None
    create_at: DATETIME | None
