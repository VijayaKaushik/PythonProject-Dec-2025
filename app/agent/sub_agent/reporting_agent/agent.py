import asyncio

from dotenv import load_dotenv
import asyncio

from google.adk.agents.llm_agent import LlmAgent


from .tool import get_tools

load_dotenv()

def get_reporting_agent():
    root_agent=LlmAgent(
        name="reporting_agent",
        model= "gemini-2.0-flash",
        description="reporting_agent is meant for creating template, listing templates and scheduling reports",
        instruction= "reporting_agent is meant for creating template, listing templates and scheduling reports",
        tools= get_tools()

    )

    #result=await agent.run_async("list all the templates")
    return root_agent

# if __name__ == "__main__":
#     asyncio.run(main())
reporting_agent= get_reporting_agent()

