"""GitHub agent: connect to the GitHub MCP through OBOT and run a ReAct agent over its tools."""
import os
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from shared_utils import create_oauth_provider


async def run_github_agent(prompt: str) -> str:
    url = os.environ["GITHUB_MCP_URL"]
    provider = create_oauth_provider(url, "GitHub MCP Agent")
    client = MultiServerMCPClient(
        {"github": {"url": url, "transport": "streamable_http", "auth": provider}}
    )
    tools = await client.get_tools(server_name="github")
    agent = create_react_agent(ChatOpenAI(model="gpt-4o", temperature=0), tools)
    result = await agent.ainvoke({"messages": [("user", prompt)]})
    return result["messages"][-1].content
