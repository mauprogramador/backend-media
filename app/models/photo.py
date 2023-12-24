from pydantic import BaseModel, Field
from datetime import datetime


class PhotoDocument(BaseModel):
    url: str = Field()
    blob: str = Field()
    upload_at: datetime = Field(default_factory=datetime.now)
