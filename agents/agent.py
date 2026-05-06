import datetime
from strands import Agent
from strands.models.ollama import OllamaModel

# 1. Define a simple local tool
def get_current_time():
    """Returns the current system time."""
    return datetime.datetime.now().strftime("%I:%M %p")

# system_prompt = "You are a respectful agent. You give answers in a kind and humble way."
# 2. Setup Model
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2:1b"
)

# 3. Initialize Agent with the local tool
agent = Agent(
    model=ollama_model,
    tools=[get_current_time], # Add your function here
   
)

# 4. Run
agent("What is the current time in Pune?")