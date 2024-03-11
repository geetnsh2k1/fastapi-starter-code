import logging
from contextlib import asynccontextmanager
from logging.config import dictConfig
from os import path

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from src.commons.config.database import engine, Base
from src.commons.controllers import common_controller
from src.commons.exceptions.app_exception import AppException
from src.commons.utils.api_response import ErrorResponse
from src.commons.utils.exception_handlers import validation_exception_handler, app_exception_handler, \
    http_exception_handler
from src.commons.utils.exception_response import RequestValidationErrorResponse

log_file_path = path.join(path.dirname(path.abspath(__file__)), './logging.config')

logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine, checkfirst=True)
    yield


app = FastAPI(
    lifespan=lifespan,
    exception_handlers={
        RequestValidationError: validation_exception_handler,
        AppException: app_exception_handler,
        HTTPException: http_exception_handler
    },
    responses={
        500: {
            "description": "App Exception",
            "model": ErrorResponse
        },
        422: {
            "description": "Validation Error",
            "model": RequestValidationErrorResponse,
        },
        400: {
            "description": "HTTP Exception",
            "model": ErrorResponse,
        }
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(common_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
