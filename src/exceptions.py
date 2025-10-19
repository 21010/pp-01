class RequestError(Exception):
    """Obsługa wyjątków (4xx, 5xx)"""

    def __init__(self, message="Błąd żądania"):
        self.message = message
        super().__init__(self.message)


class NotFoundError(RequestError):
    """Obsługa wyjątków (404)"""

    def __init__(self, message="Nie znaleziono pliku"):
        super().__init__(message)
        print(message)


class AccessDeniedError(RequestError):
    """Obsługa wyjątków (403)"""

    def __init__(self, message="Brak dostępu do pliku"):
        super().__init__(message)
        print(message)
