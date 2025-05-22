# KnowledgeBoxAI MCP

[MCP server](https://modelcontextprotocol.io/introduction) for [KnowledgeBoxAI](https://app--knowledge-box-ai-78f29a8f.base44.app) (currently based on [Base44](https://base44.app))

## Available tools in this MCP server

* `get_current_user` - Get information about current user.
* `get_knowledge_boxes` - Get Knowledge Boxes.
* `get_documents` - Get Documents per Knowledge Box ID.

## Running with Podman or Docker

You can run the KnowledgeBoxAI MCP server in a container using Podman or Docker:

Example configuration for running with Podman:

```json
{
  "mcpServers": {
    "knowledgeboxai-mcp": {
      "command": "podman",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "BASE44_API_KEY",
        "spacesketchai/knowledgeboxai-mcp:latest"
      ],
      "env": {
        "BASE44_API_KEY": "REDACTED"
      }
    }
  }
}
```

Replace `REDACTED` with the API key from https://base44.app/user-settings.
