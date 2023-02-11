from app.pkg.models.base import BaseAPIException


__all__ = ["UniqueViolation", "EmptyResult", "DriverError"]


class UniqueViolation(BaseAPIException):
    message = "Not unique"
    status_code = 409


class EmptyResult(BaseAPIException):
    message = "Empty result"
    status_code = 404


class DriverError(BaseAPIException):
    def __init__(self, message: str = None):
        if message:
            self.message = message

    message = "Internal driver error"
    status_code = 500
