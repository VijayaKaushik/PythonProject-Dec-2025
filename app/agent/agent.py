from google.adk.agents import Agent

from .sub_agent.reporting_agent.agent import reporting_agent



root_agent= Agent(
    name="Manager",
    model= "gemini-2.0-flash",
    description="Manger agent ",
    instruction ="Manager Agent",
    sub_agents= [reporting_agent]
)

