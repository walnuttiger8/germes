from pydantic import BaseModel


class RegisterUser(BaseModel):
    login: str
    password_hash: str
