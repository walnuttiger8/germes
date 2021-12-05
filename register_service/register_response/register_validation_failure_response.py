from models.shared.validation_result import FailureValidationResult
from .base.register_failure_response import RegisterFailureResponse


class RegisterValidationFailureResponse(RegisterFailureResponse):

    def __init__(self, validation_result: FailureValidationResult):
        self._validation_result = validation_result

    @property
    def validation_result(self):
        return self._validation_result
