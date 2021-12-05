from abc import ABC

from application.models import Registry
from application.repository.base import IRepository


class IRegistryRepository(IRepository[Registry], ABC):
    pass
