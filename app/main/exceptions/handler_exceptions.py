from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from . import (
    HttpException,
    BaseExceptionResponse,
    PydanticValidationExceptionResponse,
    ValidationErrorResponse
)
from pydantic_core import ValidationError
import sys


class ExceptionHandler:
    @classmethod
    def handlers(cls):
        return {
            RequestValidationError: cls.fastapi_validation_error_handler,
            ResponseValidationError: cls.fastapi_validation_error_handler,
            ValidationError: cls.pydantic_validation_error_handler,
            HttpException: cls.http_exception_handler,
            Exception: cls.exception_handler
        }

    async def fastapi_validation_error_handler(_, exception: RequestValidationError | ResponseValidationError):
        response = ValidationErrorResponse(message=str(exception.body), detail=exception.errors())
        return JSONResponse(response.model_dump(), 400)

    async def pydantic_validation_error_handler(_, exception: ValidationError):
        response = PydanticValidationExceptionResponse.make(exception)
        return JSONResponse(response.model_dump(), 500)

    async def http_exception_handler(_, exception: HttpException):
        return JSONResponse(exception.dict(), exception.status_code)

    async def exception_handler(_, exception: Exception):
        exception_type, exception_value, _ = sys.exc_info()
        exception_name = getattr(exception_type, "__name__", "Exception")
        message = f"Unexpected Error <{exception_name}({exception_value}): Args: {exception.args}>"
        response = BaseExceptionResponse(message=message)
        return JSONResponse(response.model_dump(), 500)
