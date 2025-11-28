from agno.agent import Agent
from agno.tools.models.groq import GroqTools
from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    instructions=[
        "You are a helpful assistant that can transcribe audio, translate text and generate speech."
    ],
    tools=[GroqTools()],
)

response = agent.run("Explain Snowflake Cortex Search simply")
print(response.content)
