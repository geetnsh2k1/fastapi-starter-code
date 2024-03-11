from typing import Any, Union


class AppException(Exception):
    def __init__(self, error_code: int, error_message: str, error: Union[Any, None] = None, status_code: int = 500):
        self.status_code = status_code
        self.error_code = error_code
        self.error_message = error_message
        self.error = error
        super().__init__(self.error_message)
