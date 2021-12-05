from pydantic import BaseModel
from .registry_value_type import RegistryValueType


class RegistryColumn(BaseModel):
    id: int
    registry_id: int
    name: str
    value_type: RegistryValueType
