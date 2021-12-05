from pydantic import BaseModel


class RegistryValueType(BaseModel):
    id: int = None
    name: str
    value_type: str
