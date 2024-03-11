from pydantic import BaseModel


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""
    # # Logging config
    version: int = 1
    disable_existing_loggers: bool = False
