from abc import ABC

from application.models import RegistryColumn
from application.repository.base import IRepository


class IRegistryColumnRepository(IRepository[RegistryColumn], ABC):
    pass
