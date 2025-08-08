
from agents.base_agent import Agent
from guardrails.input_guardrail import bank_input_guardrail

guardrail_agent = Agent(
    name="Guardrail Agent",
    goal="Check if the user is asking bank-related questions.",
    input_guardrails=[bank_input_guardrail]
)
