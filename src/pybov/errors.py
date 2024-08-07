"""
Module to host error classes and utilities.
"""
class PybovError(Exception):
    """
    Base exception to be eithe risen or inherited by
    other error classes.
    """
    message: str
    code: int = 1

    def __init__(self, message: str, code: int = 1) -> None:
        """
        Create a new error instance, requiring a error message
        and an optional error code (defaults to 1).
        """
        super().__init__(message)

        self.message = message
        self.code = code

    def __str__(self) -> str:
        """
        Return a user friendly string reprensentation
        of the error.
        """
        return self.message

    def __repr__(self) -> str:
        """
        Return a string reprensentation of the error
        for testing/debugging purposes.
        """
        return f'[{self.code}] {self.message}'
