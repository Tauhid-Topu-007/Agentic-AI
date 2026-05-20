from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb  # Fixed import
from rich.pretty import pprint

load_dotenv()

# Create SQLite database instance
db = SqliteDb(db_file="agno.db")  # Fixed class name
db.clear_memories()  # Clear existing memories

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        db=db,  # Database for persistent memory
        markdown=True,
        add_history_to_context=True,  # Adds conversation history to context
        enable_user_memories=True,  # ✅ Fixed: plural 'memories'
    )

# Create the agent
agent = build_agent()

user_id = 'topu@gmail.com'

# The agent will now remember context between responses
agent.print_response("What is the capital of Bangladesh?", user_id=user_id)

# The second response will use memory of the previous conversation
agent.print_response("What is the best time to visit it?", user_id=user_id)

memories=agent.db.get_user_memories(user_id=user_id)  # ✅ Fixed: get_memories method
print("\n" + "=" * 50)
print("Memories stored for user:")
print("=" * 50)
pprint(memories)