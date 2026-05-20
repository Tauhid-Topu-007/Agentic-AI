from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

from agno.tools.duckduckgo import DuckDuckGoTools

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools()],
        description="Share 15-minute healthy recipes.",
        markdown=True,
        instructions=(
            "You are a helpful assistant that shares 15-minute healthy recipes. "
            "You will be given a list of ingredients and you will share a recipe "
            "that can be made with those ingredients. You will also share the "
            "cooking time and servings, and present everything in markdown format."
        ),
        add_datetime_to_context=True
    )

# Create the agent
agent = build_agent()

# Get a recipe response
agent.print_response(
    "is it safe to travel UAE today?"
)