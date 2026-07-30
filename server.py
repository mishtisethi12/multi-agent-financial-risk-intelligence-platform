from fastmcp import FastMCP

mcp = FastMCP("Financial Risk Server")


@mcp.tool()
def hello():
    return "Hello from Financial MCP Server!"


@mcp.tool()
def get_portfolio_value():
    return 98052.13


@mcp.tool()
def get_sharpe_ratio():
    return 0.13


@mcp.tool()
def get_var():
    return 2532.27


@mcp.tool()
def get_sentiment():
    return "POSITIVE"


@mcp.tool()
def get_latest_news():
    return "Tesla misses on earnings, as free cash flow turns negative."


@mcp.tool()
def get_recommendation():
    return "Hold current positions and continue monitoring market conditions."


if __name__ == "__main__":
    mcp.run()