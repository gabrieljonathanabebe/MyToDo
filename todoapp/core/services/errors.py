# todoapp/core/services/errors.py

from todoapp.core.results import Code


# ===== BASE CLASS ============================================================
class ServiceError(Exception):
    default_message = 'Service error.'

    def __init__(self, message: str | None = None):
        self.message = message or self.default_message
        super().__init__(self.message)

    @property
    def code(self) -> Code:
        raise NotImplementedError
    

# ===== INVALID INPUT =========================================================
class InvalidInputError(ServiceError):
    default_message = 'Invalid input.'

    @property
    def code(self) -> Code:
        return Code.INVALID_INPUT
    

# ===== NOT FOUND =============================================================
class NotFoundError(ServiceError):
    default_message = 'Resource not found.'

    @property
    def code(self) -> Code:
        return Code.NOT_FOUND
    

# ===== ALREADY EXISTS ======================================================== 
class AlreadyExistsError(ServiceError):
    default_message = 'Resource already exists.'

    @property
    def code(self) -> Code:
        return Code.ALREADY_EXISTS
    

# ===== UNAUTHORIZED ==========================================================
class UnauthorizedError(ServiceError):
    default_message = 'Unauthorized.'

    @property
    def code(self) -> Code:
        return Code.UNAUTHORIZED