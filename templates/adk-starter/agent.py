"""Minimal Google ADK agent with one example tool.

ADD YOUR TOOLS HERE: define a plain function with a docstring and add it to
the tools list. Change the model where marked MODEL.
"""

from google.adk.agents import Agent


def get_current_time() -> str:
    """Returns the current date and time. Use when the user asks about time."""
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


root_agent = Agent(
    name="starter_agent",
    model="gemini-2.0-flash",  # MODEL: change the model here
    description="A starter agent that answers questions and can tell the time.",
    instruction=(
        "You are a helpful assistant. Answer clearly and concisely. "
        "Use the get_current_time tool when the user asks about the current time."
    ),
    tools=[get_current_time],  # ADD YOUR TOOLS HERE
)
