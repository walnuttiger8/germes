from application.repository.base.irepository import IRepository
from application.models.user import User
from abc import ABC


class IUserRepository(IRepository[User], ABC):

    def get_from_login(self, login: str) -> User:
        pass
