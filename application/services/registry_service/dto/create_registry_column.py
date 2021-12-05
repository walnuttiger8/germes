from pydantic import BaseModel

from application.models import RegistryValueType


class CreateRegistryColumn(BaseModel):
    name: str
    value_type: RegistryValueType
