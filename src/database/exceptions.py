
class AlreadyExists(Exception):
    def __init__(self, message = "Email уже существует.") -> None:
        super().__init__(message)
