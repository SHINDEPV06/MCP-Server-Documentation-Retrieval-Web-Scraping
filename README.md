# MCP Server: Documentation Retrieval & Web Scraping

A Python-based Model Context Protocol server that retrieves documentation and web content using the `get_docs` tool, then uses an LLM to transform the retrieved information into a clear, human readable final answer.

**Tech Stack:** Python, FastMCP, AsyncIO, httpx, Serper API, Groq LLM API, uv, python-dotenv

## Features
- MCP tool: `get_docs(query, library)` to search docs
- Gets information from official documentation websites only
- Uses an LLM to convert retrieved data into a simple, human readable answer
- Provides the final answer with `SOURCE: links`

## Project structure

- `mcp_server.py` - MCP server and `get_docs` tool
- `client.py` - MCP client that calls the tool and asks the LLM
- `utils.py` - HTML cleaning and LLM helper
- `pyproject.toml` - dependencies and project config

## Installation

### 1. Clone the repository:
```bash
git clone <your-repo-url> mcp-server-python
cd mcp-server-python
```
### 2. Environment Variables

Create a .env file in the project root and add your API keys:
```bash
SERPER_API_KEY=your_serper_key
GROQ_API_KEY=your_groq_key
```
### 3. Install dependencies:
```bash 
uv sync
```
### 4. Run the MCP Server
```bash
uv run mcp_server.py
```
### 5. Run the client:
```bash
uv run client.py
```
### 6. Output:
```bash
Available tools: ['get_docs']
ANSWER: <final answer with SOURCE links>
```
## Claude Desktop Integration (Local MCP Setup)

- **Local MCP Integration:** Can be connected to Claude Desktop using MCP cloud configuration  
- **Tool Access:** Allows Claude to use the `get_docs` tool during chats  
- **Live Updates:** Fetches real-time documentation from official sources to generate up-to-date answers.
- **No Knowledge Cutoff:** Answers are based on current sources instead of only built-in training data. 


### Chat example (MCP in use):
https://claude.ai/share/be87f780-600f-4fdc-9043-72df54c92501
