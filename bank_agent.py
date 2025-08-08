import asyncio
import os
from dotenv import load_dotenv

from models.account_model import Account
from agents.bank_main_agent import run_bank_agent

load_dotenv()

user_context = Account(name="Mariya", pin=1234)

async def main():
    print("🤖 Bank Agent is running...")
    result = await run_bank_agent("What is the balance of account 30943883", context=user_context)
    print("🟢 Response:", result)

if __name__== "__main__":
  asyncio.run(main())

