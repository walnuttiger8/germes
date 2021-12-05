from pydantic import BaseModel
from .registry_column import RegistryColumn


class RegistryRecord(BaseModel):
    id: int = None
    registry_id: int = None
    value: str
    column: RegistryColumn
