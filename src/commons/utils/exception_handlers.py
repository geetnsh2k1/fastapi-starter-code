from typing import Union, Any

from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from src.commons.exceptions.app_exception import AppException
from src.commons.utils.api_response import ErrorResponse
from src.commons.utils.exception_response import RequestValidationError


def generate_error_response(
        status_code: int,
        error_code: int,
        message: str, error: Union[Any, None] = None
):
    return JSONResponse(
        content=jsonable_encoder(
            ErrorResponse(
                status_code=error_code,
                message=message,
                error=jsonable_encoder(error),
            )
        ),
        status_code=status_code,
    )


async def http_exception_handler(
        request: Request, exc: HTTPException
):
    return generate_error_response(
        status_code=exc.status_code,
        error_code=exc.status_code,
        message="HTTP Exception",
        error=exc.detail
    )


async def validation_exception_handler(
        request: Request, exc: RequestValidationError
):
    errors = exc.errors()
    try:
        errors = [
            RequestValidationError(
                type=err["type"],
                field_name=err["loc"][1],
                message=err["msg"])
            for err in exc.errors()
        ]
    except Exception as e:
        print(f"Failed to create custom validation error response due to ${e}")

    return generate_error_response(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        error_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        message="Validation Error",
        error=errors
    )


async def app_exception_handler(
        request: Request, exc: AppException
):
    return generate_error_response(
        status_code=exc.status_code,
        error_code=exc.error_code,
        message=exc.error_message,
        error=exc.error
    )
