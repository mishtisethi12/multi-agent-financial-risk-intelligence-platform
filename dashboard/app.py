import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Financial Risk Dashboard",
    page_icon="📈",
    layout="wide"
)

# Title
st.title("📈 Financial Risk Dashboard")
st.markdown("### AI-Powered Portfolio Analytics using MCP")

# Metrics Row
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Portfolio Value", "$98,052.13")

with col2:
    st.metric("Sharpe Ratio", "0.13")

with col3:
    st.metric("Value at Risk", "$2,532.27")

st.divider()

# Sentiment and Recommendation
col4, col5 = st.columns(2)

with col4:
    st.subheader("Market Sentiment")
    st.success("POSITIVE")

with col5:
    st.subheader("Recommendation")
    st.info(
        "Hold current positions and continue monitoring market conditions."
    )

st.divider()

# Latest News
st.subheader("Latest News")

news = [
    "Tesla misses on earnings, as free cash flow turns negative.",
    "Tesla releases Q2 2026 financial results.",
    "Alphabet beats Wall Street expectations.",
    "Big Tech earnings continue to drive market movement."
]

for item in news:
    st.write(f"- {item}")

st.divider()

# Charts
st.subheader("Generated Charts")

st.image("Charts/portfolio_allocation.png",
         caption="Portfolio Allocation")

st.image("Charts/sector_allocation.png",
         caption="Sector Allocation")

st.image("Charts/daily_returns.png",
         caption="Daily Returns")

st.divider()

# MCP Section
st.subheader("MCP Server Status")

st.success("Financial Risk MCP Server Running Successfully")

# Footer
st.markdown("---")
st.markdown(
    "Built using Python, Streamlit, yFinance, FastMCP, Pandas, and Matplotlib."
)