from google import genai
import streamlit as st


from server import (
    get_portfolio_value,
    get_sharpe_ratio,
    get_var,
    get_sentiment,
    get_latest_news,
    get_recommendation
)
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)



def ask_gemini(question):

    prompt = f"""
You are an Expert Financial Risk Analyst.

Analyze the following portfolio metrics.

Portfolio Value: ${get_portfolio_value()}

Sharpe Ratio: {get_sharpe_ratio()}

Value at Risk (95%): ${get_var()}

Market Sentiment:
{get_sentiment()}

Latest News:
{get_latest_news()}

Recommendation:
{get_recommendation()}

Answer the user's question professionally.

User Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    while True:

        q = input("Ask: ")

        if q.lower() == "exit":
            break

        try:
            print("\nGemini:\n")
            print(ask_gemini(q))

        except Exception as e:
            print(e)