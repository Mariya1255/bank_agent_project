from agents.base_agent import Agent
from tools.balance_tool import check_balance

balance_agent = Agent(
    name="Balance Agent",
    goal="Provide balance details to user.",
    tools=[check_balance]
)
