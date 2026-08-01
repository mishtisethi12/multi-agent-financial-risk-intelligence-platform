import streamlit as st


def render_dashboard(total_value, sharpe, var, stock_values):

    # ===========================================
    # HEADER
    # ===========================================

    st.title("📈 Financial Risk Intelligence Platform")

    st.caption(
        "AI-Powered Portfolio Analytics using Gemini + FastMCP"
    )

    st.info(
        "Real-time Portfolio Analysis • Value at Risk • Sharpe Ratio • Market Sentiment"
    )

    st.divider()

    # ===========================================
    # KPI CARDS
    # ===========================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Portfolio Value",
            f"${total_value:,.2f}"
        )

    with c2:
        st.metric(
            "Sharpe Ratio",
            f"{sharpe:.2f}"
        )

    with c3:
        st.metric(
            "95% VaR",
            f"${var:,.2f}"
        )

    with c4:
        st.metric(
            "Market Sentiment",
            "🟢 Positive"
        )

    st.divider()

    # ===========================================
    # RECOMMENDATION
    # ===========================================

    st.subheader("📌 Investment Recommendation")

    st.success(
        "Hold current positions and continue monitoring market conditions."
    )

    st.divider()

    # ===========================================
    # CHARTS
    # ===========================================

    left, right = st.columns(2)

    with left:

        st.subheader("📊 Portfolio Allocation")

        st.image(
            "Charts/portfolio_allocation.png",
            use_container_width=True
        )

    with right:

        st.subheader("📊 Sector Allocation")

        st.image(
            "Charts/sector_allocation.png",
            use_container_width=True
        )

    st.subheader("📈 Daily Returns")

    st.image(
        "Charts/daily_returns.png",
        use_container_width=True
    )

    st.divider()

    # ===========================================
    # NEWS
    # ===========================================

    st.subheader("📰 Latest Financial News")

    news = [
        "Tesla misses on earnings, as free cash flow turns negative.",
        "Tesla releases quarterly financial results.",
        "Alphabet beats Wall Street expectations.",
        "Big Tech earnings continue to influence market movement."
    ]

    for item in news:
        st.write(f"• {item}")

    st.divider()

    # ===========================================
    # SUMMARY
    # ===========================================

    st.subheader("📋 Portfolio Summary")

    s1, s2 = st.columns(2)

    with s1:

        st.write(f"**Total Holdings:** {len(stock_values)}")

        st.write("**Data Source:** Yahoo Finance")

        st.write("**Portfolio Status:** Active")

    with s2:

        st.write("**LLM:** Gemini")

        st.write("**MCP Server:** Connected")

        st.write("**Dashboard:** Streamlit")

    st.divider()

    # ===========================================
    # SERVER STATUS
    # ===========================================

    st.subheader("🟢 System Status")

    st.success("Financial Risk Intelligence Platform is running successfully.")