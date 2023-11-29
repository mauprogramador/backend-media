from pydantic import BaseModel
from pydantic_core import ValidationError


class BaseExceptionResponse(BaseModel):
    success: bool = False
    message: str


class PydanticValidationExceptionResponse(BaseModel):
    success: bool = False
    message: str
    detail: list

    @staticmethod
    def make(exception: ValidationError):
        message = "Pydantic validation error: {} validation errors for {}"
        message = message.format(exception.error_count(), exception.title)
        return PydanticValidationExceptionResponse(message=message, detail=exception.errors())


class ValidationErrorResponse(BaseModel):
    success: bool = False
    message: str
    detail: list
