import asyncio
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

llm = ChatOpenAI()


load_dotenv()
llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/shakilsh/projects/langchain-project/mcp-course/mcp-course/servers/math_server.py"],
)

async def main():
    print("hello from mcp-course!")

