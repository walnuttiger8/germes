from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    login: str
    password_hash: str

