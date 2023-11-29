from pydantic import BaseModel, Field


class TokenModelOut(BaseModel):
    issuer: str = Field(validation_alias="iss")
    subject: str = Field(validation_alias="sub")
    expiration: int = Field(validation_alias="exp")
    service: str = Field()
