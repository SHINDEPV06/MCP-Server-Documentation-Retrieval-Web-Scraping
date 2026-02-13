import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
import os
from dotenv import load_dotenv

from utils import get_response_from_llm


load_dotenv()

server_params = StdioServerParameters(
    command="uv",
    args=["run", "mcp_server.py"],
    env=None,
    )

async def main():

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            tools_response = await session.list_tools()
            print("Available tools:", [t.name for t in tools_response.tools])

            query = "how to install uv package?"
            library = "uv"
            res = await session.call_tool("get_docs", arguments = {"query": query, "library": library})

            context = res.content
            user_prompt_with_context = f"Query: {query}, Context {context}"

            # LLM function to create a human readable response
            SYSTEM_PROMPT= """
            Answer the question based on the provided context. If you don't know the answer, say you don't know. Always keep the answer concise and to the point.
            Keep every 'SOURCE:' line exactly; list sources at the end.
            give the answer in a human readable format, not in a json format. Do not include any tool calls in the answer.
            answer in structured format with sources at the end, & stepwise fromat.
            answer mustbe in text format not in  markdown format. Do not include any code blocks in the answer.

            """
            answer = get_response_from_llm(user_prompt=user_prompt_with_context, system_prompt=SYSTEM_PROMPT, model="openai/gpt-oss-120b")
            print("ANSWER: ", answer)

if __name__ == "__main__":
    asyncio.run(main())