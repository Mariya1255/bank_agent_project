from agents.base_agent import Agent
from tools.transfer_tool import transfer_money

transfer_agent = Agent(
    name="Transfer Agent",
    goal="Help transfer money between accounts.",
    tools=[transfer_money]
)
