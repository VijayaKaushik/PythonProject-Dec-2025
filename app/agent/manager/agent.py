from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent

from .sub_agent.knowledge_base_agent.agent import knowledge_base_agent
from .sub_agent.reporting_agent.agent import reporting_agent

load_dotenv()
# uncomment to run via adk web
# root_agent = LlmAgent(
#     name="Manager",
#     model="gemini-2.5-flash",
#     description="Manager agent",
#     instruction="Routes tasks to sub agents",
#     sub_agents=[reporting_agent],
# )


manager_agent = LlmAgent(
    name="Manager",
    model="gemini-2.5-flash",
    description="Manager agent",
    instruction="Routes tasks to sub agents",
    sub_agents=[reporting_agent,knowledge_base_agent],
)

