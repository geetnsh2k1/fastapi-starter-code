from typing import Any, Union

from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    status_code: int
    message: str


class Response(BaseResponse):
    data: Union[None, Any]


class ErrorResponse(BaseResponse):
    error: Union[None, Any]


class PaginatedData(BaseModel):
    current_page: int
    total_pages: int
    page_size: int
