from repository.user.base.iuser_repository import IUserRepository
from models.user import User
from models.shared.validation_result import IValidationResult, ValidationComment, FailureValidationResult, SuccessValidationResult


class UserValidationService:

    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    def validate_user(self, user: User) -> IValidationResult:
        comments: list[ValidationComment] = list()

        if self._user_repository.get_from_login(user.login):
            comments.append(ValidationComment("login", f"login '{user.login}' must be unique"))

        if comments:
            return FailureValidationResult(comments)
        return SuccessValidationResult()
