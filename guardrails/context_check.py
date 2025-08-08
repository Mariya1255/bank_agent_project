
from agents.base_agent import RunContextWrapper

def check_user(ctx: RunContextWrapper, agent) -> bool:
    return ctx.context.name == "Mariya" and ctx.context.pin ==1456