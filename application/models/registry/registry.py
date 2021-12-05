from pydantic import BaseModel
from .registry_column import RegistryColumn
from .registry_record import RegistryRecord


class Registry(BaseModel):
    id: int = None
    user_id: int = None
    name: str
    columns: list[RegistryColumn] = []
    records: list[RegistryRecord] = []
