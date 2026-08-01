import streamlit as st


def render_sidebar(stock_values):

    with st.sidebar:

        st.title("📈 Financial AI")

        st.caption("Risk Intelligence Platform")

        st.divider()

        st.subheader("System Status")

        st.success("🟢 Gemini Connected")

        st.success("🟢 FastMCP Running")

        st.success("🟢 Yahoo Finance Live")

        st.divider()

        st.subheader("Portfolio Overview")

        st.metric("Holdings", len(stock_values))

        st.write("**Data Source:** Yahoo Finance")

        st.write("**Risk Model:**")

        st.write("- Value at Risk (95%)")

        st.write("- Sharpe Ratio")

        st.write("- Sentiment Analysis")

        st.divider()

        st.subheader("Technology Stack")

        st.write("• Python")

        st.write("• FastMCP")

        st.write("• Gemini")

        st.write("• Streamlit")

        st.write("• yFinance")

        st.write("• Pandas")

        st.write("• TextBlob")

        st.divider()

        st.caption("Version 1.0")