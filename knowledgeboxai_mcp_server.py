import os

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("knowledgebox-ai")

BASE44_APP_ID = os.environ.get("BASE44_APP_ID", "682e2e6ac2e09b7378f29a8f")


async def make_api_request(api_path, method="GET", data=None):
    url = f"https://base44.app/api/{api_path}"
    headers = {"api_key": os.environ["BASE44_API_KEY"], "Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        if method.upper() == "GET":
            response = await client.request(method, url, headers=headers, params=data)
        else:
            response = await client.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def get_current_user():
    """Get information about current user."""
    api_path = f"apps/{BASE44_APP_ID}/entities/User/me"
    response = await make_api_request(api_path)
    return response


@mcp.tool()
async def get_knowledge_boxes(created_by: str):
    """Get Knowledge Boxes."""
    api_path = f"apps/{BASE44_APP_ID}/entities/KnowledgeBox"
    response = await make_api_request(api_path)
    lines = []
    for item in response:
        if created_by and item["created_by"] != created_by:
            continue
        lines.append(f"KnowledgeBox Name: {item['name']}")
        lines.append(f"KnowledgeBox ID: {item['id']}")
        lines.append(f"KnowledgeBox Created by: {item['created_by']}")
        lines.append(f"KnowledgeBox description: {item['description']}")
    return "\n".join(lines)


@mcp.tool()
async def get_documents(knowledgebox_id: str):
    """Get Documents per Knowledge Box ID."""
    api_path = f"apps/{BASE44_APP_ID}/entities/Document"
    response = await make_api_request(api_path)
    lines = []
    for item in response:
        if item["knowledge_box_id"] != knowledgebox_id:
            continue
        lines.append(f"Document Name: {item['file_name']}")
        lines.append(f"Document ID: {item['id']}")
        lines.append(f"Document summary: {item['summary']}")
        lines.append(f"Document URL: {item['file_url']}")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")
