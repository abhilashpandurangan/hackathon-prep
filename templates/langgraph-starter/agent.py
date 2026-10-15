"""Minimal LangGraph ReAct agent with one example tool.

ADD YOUR TOOLS HERE: define a plain function with a docstring and add it to
the tools list. Change the model where marked MODEL.
"""

from langgraph.prebuilt import create_react_agent


def get_current_time() -> str:
    """Returns the current date and time. Use when the user asks about time."""
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


agent = create_react_agent(
    model="openai:gpt-4o-mini",  # MODEL: change the model here (any init_chat_model string works)
    tools=[get_current_time],  # ADD YOUR TOOLS HERE
    prompt="You are a helpful assistant. Answer clearly and concisely.",
)
