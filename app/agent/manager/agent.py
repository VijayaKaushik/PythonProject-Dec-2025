from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from .sub_agent.reporting_agent.agent import reporting_agent

load_dotenv()

root_agent = LlmAgent(
    name="Manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="Routes tasks to sub agents",
    sub_agents=[reporting_agent],
)
