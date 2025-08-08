from models.account_model import Account

def transfer_money(context: Account):
    # Dummy logic for transfer
    amount = 100
    if context.balance >= amount:
        context.balance -= amount
        return f"Transferred ${amount}. New balance is ${context.balance}."
    else:
        return "Insufficient funds for transfer."