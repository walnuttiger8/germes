from typing import Generic, TypeVar
from abc import ABC, abstractmethod

TEntity = TypeVar("TEntity")


class IRepository(Generic[TEntity], ABC):

    @abstractmethod
    def add(self, entity: TEntity):
        pass

    @abstractmethod
    def update(self, entity: TEntity):
        pass

    @abstractmethod
    def get_all(self) -> list[TEntity]:
        pass

    @abstractmethod
    def get(self, entity_id: int) -> TEntity or None:
        pass

    @abstractmethod
    def delete(self, entity: TEntity) -> None:
        pass
