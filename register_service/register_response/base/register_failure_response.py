from abc import ABC
from .iregister_response import IRegisterResponse


class RegisterFailureResponse(IRegisterResponse, ABC):
    pass
