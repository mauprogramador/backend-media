from pydantic import BaseModel
from datetime import datetime


class VideoModelOut(BaseModel):
    uuid: str
    url: str
    blob: str
    upload_at: datetime
