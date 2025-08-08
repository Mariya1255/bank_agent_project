from pydantic import BaseModel

class Account(BaseModel):
    name: str
    pin: int
    balance: float = 1000.0
    account_number: str = "30943883"