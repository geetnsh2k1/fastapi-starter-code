from sqlalchemy.orm import Session

from src.commons.service.common_service import CommonService


class ServiceFactory:

    @staticmethod
    def get_common_service(db: Session):
        return CommonService(db=db)
