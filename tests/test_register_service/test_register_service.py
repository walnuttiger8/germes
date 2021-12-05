from unittest import TestCase
from unittest.mock import Mock

from application.services.register_service import RegisterService
from application.services.register_service.dto import RegisterUser
from application.services.register_service.register_response import RegisterSuccessResponse
from application.services.user_validation_service import UserValidationService


class TestRegisterService(TestCase):

    def setUp(self):
        self.user_repository = Mock()
        self.user_repository.get_from_login.return_value = None

        self.validation_service = UserValidationService(self.user_repository)
        self.service = RegisterService(user_validation_service=self.validation_service,
                                       user_repository=self.user_repository)

    def tearDown(self) -> None:
        super().tearDown()

    def test_register_new_user(self):
        register_user = RegisterUser(login="first", password_hash="some-hash")
        register_response = self.service.register_new_user(register_user)

        self.assertIsInstance(register_response, RegisterSuccessResponse)
        self.assertIsNotNone(register_response.user)
        self.assertEqual(register_response.user.login, register_user.login)
        self.assertEqual(register_response.user.password_hash, register_user.password_hash)
