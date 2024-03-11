from sqlalchemy.orm import Session

from src.commons.utils.logger import Logger


class CommonService:
    _instance = None

    def __new__(cls, db: Session):
        if cls._instance is None:
            cls._instance = super(CommonService, cls).__new__(cls)
        return cls._instance

    def __init__(self, db: Session):
        self.db = db
        self.logger = Logger.get_logger()

    def test_api(self) -> str:
        self.logger.info("logging...")
        return "testing....."
