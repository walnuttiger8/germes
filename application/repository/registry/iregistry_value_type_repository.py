from abc import ABC

from application.models import RegistryValueType
from application.repository.base import IRepository


class IRegistryValueTypeRepository(IRepository[RegistryValueType], ABC):
    pass
