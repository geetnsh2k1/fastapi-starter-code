import logging
from logging.config import dictConfig

from src.commons.config.logger_config import LogConfig
from src.commons.constants.constants import UserAuthConstants


class Logger:
    @staticmethod
    def get_logger(app_name: str = UserAuthConstants.APP_NAME):
        dictConfig(LogConfig().model_dump())
        logger = logging.getLogger(app_name)
        return logger
