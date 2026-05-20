from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
load_dotenv()
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools(), YFinanceTools()],
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",  # Only ONE description
        markdown=True,
        instructions=["Use given tools whenever possible. Format your response using markdown and use tables to display data where possible."],
        add_datetime_to_context=True,
        debug=True
    )

# Create the agent
agent = build_agent()

# Get stock information
agent.print_response(
    "Share the NVDA stock price and analyst recommendations"
)