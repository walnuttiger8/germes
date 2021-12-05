from application.repository.registry import IRegistryRepository, IRegistryColumnRepository, \
    IRegistryValueTypeRepository, IRegistryRecordRepository
from application.services.registry_service.registry_response import ICreateRegistryResponse
from dto import CreateRegistry


class RegistryService:

    def __init__(self,
                 registry_repository: IRegistryRepository,
                 registry_column_repository: IRegistryColumnRepository,
                 registry_value_type_repository: IRegistryValueTypeRepository,
                 registry_record_repository: IRegistryRecordRepository):
        self._registry_repository = registry_repository
        self._registry_column_repository = registry_column_repository
        self.registry_value_type_repository = registry_value_type_repository
        self._registry_record_repository = registry_record_repository

    def create_registry(self, create_registry: CreateRegistry) -> ICreateRegistryResponse:
        pass
