from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset, SseConnectionParams


reporting_agent = LlmAgent(
    name="reporting_agent",
    model="gemini-2.0-flash",
    instruction="Handles reporting tasks",
    tools=[McpToolset(
        connection_params=SseConnectionParams(
            url="http://localhost:8000/sse"
        )
    )],
)
