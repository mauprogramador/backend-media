from pydantic import BaseModel
from datetime import datetime


class PhotoModelOut(BaseModel):
    url: str
    blob: str
    upload_at: datetime
