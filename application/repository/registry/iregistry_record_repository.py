from abc import ABC

from application.models import RegistryRecord
from application.repository.base import IRepository


class IRegistryRecordRepository(IRepository[RegistryRecord], ABC):
    pass
