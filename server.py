from fastmcp import FastMCP
from utils.finance import (
    analyze_portfolio,
    calculate_var,
    calculate_sharpe
)

mcp = FastMCP("Financial Risk Intelligence Server")


# -----------------------------
# Health Check
# -----------------------------
@mcp.tool()
def hello():
    return "Hello from Financial Risk Intelligence Server!"


# -----------------------------
# Portfolio Analysis
# -----------------------------
@mcp.tool()
def get_portfolio_value():
    total_value, _ = analyze_portfolio()
    return round(total_value, 2)


@mcp.tool()
def get_sharpe_ratio():
    total_value, _ = analyze_portfolio()
    _, volatility = calculate_var(total_value)
    return calculate_sharpe(volatility)


@mcp.tool()
def get_var():
    total_value, _ = analyze_portfolio()
    var, _ = calculate_var(total_value)
    return var


# -----------------------------
# Market Intelligence
# -----------------------------
@mcp.tool()
def get_sentiment():
    return "POSITIVE"


@mcp.tool()
def get_latest_news():
    return "Tesla misses on earnings, as free cash flow turns negative."


# -----------------------------
# Recommendation
# -----------------------------
@mcp.tool()
def get_recommendation():

    sharpe = get_sharpe_ratio()

    if sharpe < 1:
        return "Hold current positions and continue monitoring market conditions."

    return "Portfolio performance is acceptable."


if __name__ == "__main__":
    mcp.run()