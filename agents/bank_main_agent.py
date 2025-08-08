from agents.base_agent import Agent
from agents.balance_agent import balance_agent
from agents.transfer_agent import transfer_agent
from agents.guardrail_agent import guardrail_agent

async def route_request(input_text: str, context):
    if "balance" in input_text.lower():
        return await balance_agent.run(input_text, context)
    elif "transfer" in input_text.lower():
        return await transfer_agent.run(input_text, context)
    else:
        return "I can only help with balance inquiries or transfers."

bank_agent = Agent(
    name="Bank Main Agent",
    goal="Handles main banking queries and routes them to other agents.",
    tools=[lambda ctx: route_request],
    input_guardrails=guardrail_agent.input_guardrails
)

async def run_bank_agent(input_text, context):
    if "balance" in input_text.lower():
        from agents.balance_agent import balance_agent
        return await balance_agent.run(input_text, context)
    elif "transfer" in input_text.lower():
        from agents.transfer_agent import transfer_agent
        return await transfer_agent.run(input_text, context)
    else:
      return "I can only help with balance inquiries or transfers."




















#from tools.balance_tool import check_balance
#from guardrails.input_guardrail import input_guardrail
#from agents.guardrail_agent import guardrail_agent
#from agents.base_agent import  Agent,  GuardrailFunctionOutput, RunContextWrapper

#@input_guardrail
#async def check_bank_related(ctx: RunContextWrapper, agent: Agent, input) -> GuardrailFunctionOutput:
    #result = await guardrail_agent.run(input)
    #is_not_bank_related = "balance" not in input.lower() and "account" not in input.lower()
    #return GuardrailFunctionOutput(
        #output_info=result,
        #tripwire_triggered=is_not_bank_related
    #)

#bank_agent = Agent(
    #name="Bank Agent",
    #instructions="You are a helpful bank agent. Answer only banking queries.",
    #tools=[check_balance],
    #input_guardrails=[check_bank_related]
#)

