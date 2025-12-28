from google.adk.tools.mcp_tool.mcp_toolset import McpToolset,SseConnectionParams

import asyncio
def get_tools():
    async def fetch_mcp_tools():
        sse_url="http://localhost:8000/sse"

        mcp_tool_set= McpToolset(connection_params=SseConnectionParams(url=sse_url))
        tools=await mcp_tool_set.get_tools()
        # for tool in tools:
        #     print (tool.name)
        return tools
    return asyncio.run(fetch_mcp_tools())

# if __name__ == "__main__":
#     asyncio.run (fetch_mcp_tools())