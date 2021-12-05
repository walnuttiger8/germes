from unittest import TestCase
from unittest.mock import Mock

from application.models import User
from application.services.registry_service import RegistryService
from application.services.registry_service.dto import CreateRegistry, CreateRegistryColumn


class TestRegistryService(TestCase):

    def setUp(self):
        self._registry_repository = Mock()
        self._registry_record_repository = Mock()
        self._registry_column_repository = Mock()
        self._registry_value_type_repository = Mock()

        self._registry_service = RegistryService(registry_repository=self._registry_repository,
                                                 registry_record_repository=self._registry_record_repository,
                                                 registry_column_repository=self._registry_column_repository,
                                                 registry_value_type_repository=self._registry_value_type_repository)

    def test_create_registry(self):
        user = User(login="login", password="password_hash")
        columns = [CreateRegistryColumn()]
        create_registry = CreateRegistry(user=user, name="registry")
