from pydantic import BaseModel


class ApiMessage(BaseModel):
    """Model representing a generic API message with a message and error code."""

    message: str
    error_code: int
