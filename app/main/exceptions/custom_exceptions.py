from fastapi import HTTPException


class HttpException(HTTPException):
    def __init__(self, status_code: int, message: str) -> None:
        self.success = False
        self.status_code = status_code
        self.message = message
        super().__init__(status_code, message)

    def dict(self):
        return {"success": self.success, "message": self.message}


class Unauthorized(HttpException):
    def __init__(self, message: str) -> None:
        super().__init__(401, message)


class Forbidden(HttpException):
    def __init__(self, message: str) -> None:
        super().__init__(403, message)


class NotFound(HttpException):
    def __init__(self, prefix: str) -> None:
        super().__init__(404, f"{prefix} not found")


class Conflict(HttpException):
    def __init__(self, message: str) -> None:
        super().__init__(409, message)


class InvalidUuid(HttpException):
    def __init__(self, prefix: str) -> None:
        super().__init__(422, f"Invalid {prefix} UUID")


class RequiredQueryParam(HttpException):
    def __init__(self, prefix: str) -> None:
        super().__init__(422, f"{prefix} query param is required")


class RequiredRequestBody(HttpException):
    def __init__(self) -> None:
        super().__init__(422, "Request body is required")


class InternalError(HttpException):
    def __init__(self, message: str) -> None:
        super().__init__(500, message)


class FailedDependency(HttpException):
    def __init__(self, message: str) -> None:
        super().__init__(424, message)
