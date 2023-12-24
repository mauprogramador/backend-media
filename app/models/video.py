from pydantic import BaseModel, Field
from datetime import datetime


class VideoDocument(BaseModel):
    uuid: str = Field(validation_alias="video_uuid")
    url: str = Field()
    blob: str = Field()
    upload_at: datetime = Field(default=datetime.now())
