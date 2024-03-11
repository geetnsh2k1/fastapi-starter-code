from pydantic import BaseModel, Field

from src.commons.utils.api_response import ErrorResponse


class RequestValidationError(BaseModel):
    type: str = Field(..., description="Type")
    field_name: str = Field(..., description="Field Name")
    message: str = Field(..., description="Message")


class RequestValidationErrorResponse(ErrorResponse):
    error: list[RequestValidationError] = Field(..., description="validation errors")
