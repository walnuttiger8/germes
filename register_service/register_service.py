from models import User
from models.shared.validation_result import FailureValidationResult
from .dto import RegisterUser
from .register_response import IRegisterResponse, RegisterValidationFailureResponse, \
    RegisterSuccessResponse
from repository.user.base.iuser_repository import IUserRepository
from user_validation_service import UserValidationService


class RegisterService:

    def __init__(self, user_repository: IUserRepository, user_validation_service: UserValidationService):
        self._user_repository = user_repository
        self._user_validation_service = user_validation_service

    @staticmethod
    def _user_from_register_user(register_user: RegisterUser):
        register_user_data = register_user.dict()
        return User.parse_obj(register_user_data)

    def register_new_user(self, register_user: RegisterUser) -> IRegisterResponse:
        user = RegisterService._user_from_register_user(register_user)

        validation_result = self._user_validation_service.validate_user(user)

        if isinstance(validation_result, FailureValidationResult):
            return RegisterValidationFailureResponse(validation_result)

        self._user_repository.add(user)
        return RegisterSuccessResponse(user)
