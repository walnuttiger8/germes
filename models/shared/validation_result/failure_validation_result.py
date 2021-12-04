from .base import ValidationComment, IValidationResult


class FailureValidationResult(IValidationResult):

    def __init__(self, comments: list[ValidationComment]):
        self._comments = comments

    @property
    def comments(self):
        return self._comments
