from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("add工具开始被调用...")
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("multiply工具开始被调用...")
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")