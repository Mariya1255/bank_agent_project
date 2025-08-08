
from guardrails.context_check import check_user
from models.account_model import Account

def check_balance(context: Account):
    return f"Your current balance is ${context.balance}"

def function_tool(is_enabled=None):
    def decorator(func):
        func._is_enabled = is_enabled
        return func
    return decorator

@function_tool(is_enabled=check_user)
def check_balance(account_number: str) -> str:
    return f"The balance of account {account_number} is $1,000,000"