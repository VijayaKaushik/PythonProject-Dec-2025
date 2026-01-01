from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset, SseConnectionParams


knowledge_base_agent = LlmAgent(
    name="knowledge_base_agent",
    model="gemini-2.5-flash",
    instruction="Handles questions from knowledge base : information on plans , workflows ,release notes",
    tools=[McpToolset(
        connection_params=SseConnectionParams(
            url="http://localhost:8002/sse"
        )
    )],
)
