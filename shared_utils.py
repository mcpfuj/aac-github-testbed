"""Auth helpers for reaching the GitHub MCP server through the OBOT gateway."""
import os
import httpx


class StaticBearerAuth(httpx.Auth):
    """Attach a fixed bearer token (the OBOT gateway token) to every request."""

    def __init__(self, token: str):
        self._token = token

    def auth_flow(self, request):
        request.headers["Authorization"] = f"Bearer {self._token}"
        yield request


def create_oauth_provider(server_url: str, client_name: str):
    token = os.getenv("OBOT_MCP_TOKEN", "").strip()
    if token:
        return StaticBearerAuth(token)
    raise RuntimeError("OBOT_MCP_TOKEN is not set (expected the console-injected gateway token).")
