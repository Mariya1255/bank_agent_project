from agents.base_agent import GuardrailFunctionOutput

async def bank_output_guardrail(context_wrapper, agent, output_text: str):
    # Block if sensitive info
    if "account number" in output_text.lower():
        return GuardrailFunctionOutput(output_info="Sensitive data detected", tripwire_triggered=True)
    return GuardrailFunctionOutput(output_info="Output safe", tripwire_triggered=False)


