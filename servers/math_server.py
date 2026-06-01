from mcp.server.fastmcp import FastMCP
mcp = FastMCP("math")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

# Stdio transport uses standard input and output for communication
# This is ideal for local processes.
if __name__ == "__main__":
    mcp.run(transport="stdio")