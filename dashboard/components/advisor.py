import streamlit as st
from llm import ask_gemini


def render_advisor():

    st.title("🤖 AI Financial Advisor")

    st.caption("Powered by Google Gemini")

    st.divider()

    st.markdown(
        """
Ask questions about your portfolio, market conditions,
risk metrics, diversification, or investment strategies.
"""
    )

    question = st.text_area(
        "Ask your question",
        placeholder="Example: Should I reduce my Tesla exposure?",
        height=150
    )

    col1, col2 = st.columns([1, 5])

    with col1:
        analyze = st.button(
            "🚀 Analyze",
            use_container_width=True
        )

    with col2:
        clear = st.button(
            "🗑 Clear",
            use_container_width=True
        )

    if clear:
        st.rerun()

    if analyze:

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Gemini is analyzing your portfolio..."):

                try:

                    answer = ask_gemini(question)

                    st.success("Analysis Complete")

                    st.markdown("## 📑 AI Response")

                    st.markdown(
                        f"""
<div style="
padding:25px;
border-radius:15px;
border:1px solid #d1d5db;
background-color:rgba(255,255,255,0.05);
">

{answer}

</div>
""",
                        unsafe_allow_html=True
                    )

                except Exception as e:

                    st.error(e)

    st.divider()

    st.subheader("💡 Example Questions")

    st.markdown("""
- Should I rebalance my portfolio?

- Is my portfolio diversified?

- Explain the Sharpe Ratio.

- Explain Value at Risk.

- Which stock contributes the most risk?

- Is Tesla a risky investment?

- What sectors dominate my portfolio?

- Suggest ways to reduce portfolio risk.
""")