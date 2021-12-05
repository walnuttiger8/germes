from .base.iregister_response import IRegisterResponse
from application.models.user import User


class RegisterSuccessResponse(IRegisterResponse):

    def __init__(self, user: User):
        self._user = user

    @property
    def user(self):
        return self._user
