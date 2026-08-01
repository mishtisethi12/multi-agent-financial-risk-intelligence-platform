import streamlit as st
import pandas as pd


def render_portfolio():

    st.title("📊 Portfolio Management")

    st.caption("Live Portfolio Holdings")

    st.divider()

    # -----------------------------
    # LOAD PORTFOLIO
    # -----------------------------

    portfolio = pd.read_csv("data/portfolio.csv")

    # -----------------------------
    # TABLE
    # -----------------------------

    st.subheader("Portfolio Holdings")

    st.dataframe(
        portfolio,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # -----------------------------
    # QUICK STATS
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Holdings",
            len(portfolio)
        )

    with col2:
        st.metric(
            "Total Shares",
            int(portfolio["Shares"].sum())
        )

    st.divider()

    # -----------------------------
    # DOWNLOAD CSV
    # -----------------------------

    st.download_button(
        label="⬇ Download Portfolio CSV",
        data=portfolio.to_csv(index=False),
        file_name="portfolio.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # INFORMATION
    # -----------------------------

    st.info(
        """
This portfolio is analyzed using:

• Yahoo Finance Live Data

• Value at Risk (95%)

• Sharpe Ratio

• Sentiment Analysis

• AI Recommendation Engine
"""
    )