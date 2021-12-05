from pydantic import BaseModel

from application.models import User
from .create_registry_column import CreateRegistryColumn


class CreateRegistry(BaseModel):
    name: str
    columns: list[CreateRegistryColumn]
    user: User
