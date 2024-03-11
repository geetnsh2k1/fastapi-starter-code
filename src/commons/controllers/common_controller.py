from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.commons.dependencies.db_dependency import get_db
from src.commons.factory.service_factory import ServiceFactory
from src.commons.utils.api_response import Response

router = APIRouter()


@router.get(
    path="/test",
    summary="Test-API",
    response_model=Response,
    tags=["COMMON"]
)
def test_api(
        db: Session = Depends(get_db),
):
    return Response(
        status_code=status.HTTP_200_OK,
        message="Test-API",
        data=ServiceFactory.get_common_service(db=db).test_api()
    )
