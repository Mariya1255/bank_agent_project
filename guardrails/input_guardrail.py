from agents.base_agent import GuardrailFunctionOutput, RunContextWrapper

async def bank_input_guardrail(context_wrapper, agent, input_text: str):
    # Simple check: allow only if message contains 'balance' or 'transfer'
    allowed_keywords = ["balance", "transfer"]
    if any(word in input_text.lower() for word in allowed_keywords):
        return GuardrailFunctionOutput(output_info="Safe input", tripwire_triggered=False)
    return GuardrailFunctionOutput(output_info="Unsafe input", tripwire_triggered=True)



