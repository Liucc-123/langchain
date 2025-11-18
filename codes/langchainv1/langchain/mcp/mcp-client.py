import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
import os, dotenv

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")

# 无状态的MCP服务
client = MultiServerMCPClient(
    {
        "math": {
            "transport": "stdio",  # Local subprocess communication
            "command": "python",
            # Absolute path to your math_server.py file
            "args": ["D:\code\py\langchain\codes\langchainv1\langchain\mcp\mcp-server-stdio.py"],
        },
        "weather": {
            "transport": "streamable_http",  # HTTP-based remote server
            # Ensure you start your weather server on port 8000
            "url": "http://localhost:8000/mcp",
        }
    }
)


async def main():
    tools = await client.get_tools()
    agent = create_agent(
        model="gpt-5-mini",
        tools=tools,
    )
    # math_response = await agent.ainvoke(
    #     {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    # )
    # print(math_response["messages"][-1].pretty_print())
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )
    print(weather_response["messages"][-1].pretty_print())

if __name__ == '__main__':
    asyncio.run(main())
