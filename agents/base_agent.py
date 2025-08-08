from typing import List, Optional, Any
from models.account_model import Account
from pydantic import BaseModel

class GuardrailFunctionOutput:
    def __init__(self, output_info: Any, tripwire_triggered: bool):
        self.output_info = output_info
        self.tripwire_triggered = tripwire_triggered
    

class RunContextWrapper:
    def __init__(self, context: Account):
        self.context = context


class Agent:
    def __init__(self,
                 name: str,
                 goal: Optional[str] = None,
                 instructions: Optional[str] = None,
                 tools: Optional[List[callable]] = None,
                 input_guardrails: Optional[List[callable]] = None,
                 output_type: Optional[Any] = None):
        self.name = name
        self.goal = goal
        self.instructions = instructions
        self.tools = tools or []
        self.input_guardrails = input_guardrails or []
        self.output_type = output_type
        
    

    async def run(self, input_text: str, context: Account = None):
      
       print(f"Agent '{self.name}' received input: {input_text}")
        

       # Input guardrails
       for guardrail in self.input_guardrails:
           guard_result = await guardrail(RunContextWrapper(context), self, input_text)
           if guard_result.tripwire_triggered:
               return "❌ Input rejected by guardrails."      

       # Execute tools if the input matches a tool
       for tool in self.tools:
           if callable(tool):
              return tool(context)
        
       return f"Processed input: {input_text}"