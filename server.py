from fastmcp import FastMCP

mcp = FastMCP("server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.resource("data://config")
def get_config() -> dict:
    return {"theme": "dark", "version": "1.0"}

@mcp.resource("resource://greeting")
def get_greeting() -> str:
    """Provides a simple greeting message."""
    return "Hello from FastMCP Resources!"


if __name__ == "__main__":
    # forwarder = ngrok.forward("localhost:9000", authtoken_from_env=True)
    # print(f"Available at: {forwarder.url()}")
    mcp.run(transport="http",port=9000)