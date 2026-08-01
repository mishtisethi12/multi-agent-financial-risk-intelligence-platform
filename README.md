# Multi-Agent Financial Risk Intelligence Platform

# 📈 Multi-Agent Financial Risk Intelligence Platform

An AI-powered financial risk analytics platform that combines **Multi-Agent Systems**, **FastMCP**, **Google Gemini**, **Finnhub API**, and **Streamlit** to provide intelligent portfolio analysis, risk assessment, market sentiment analysis, and AI-driven investment recommendations.

---

## 🚀 Live Demo

🔗 **Streamlit App:** *(Add your deployment link here after deployment)*

Example:

https://your-app-name.streamlit.app

---

## ✨ Features

- 📊 Live Portfolio Valuation
- 📈 Portfolio Allocation Analysis
- 🏦 Sector Allocation Analysis
- ⚡ Live Stock Prices using Finnhub API
- 📉 Value at Risk (VaR)
- 📊 Sharpe Ratio
- 📰 Live Financial News
- 😊 Market Sentiment Analysis
- 🤖 AI Financial Advisor (Google Gemini)
- 🔌 FastMCP Financial Server
- 📋 CSV Report Generation
- 📊 Interactive Streamlit Dashboard
- ☁️ Cloud Deployment

---

## 🖼️ Dashboard Preview

> Add screenshots after uploading them.

### Dashboard

```
images/dashboard.png
```

### AI Financial Advisor

```
images/advisor.png
```

### Portfolio Analytics

```
images/portfolio.png
```

---

## 📌 Project Overview

The **Multi-Agent Financial Risk Intelligence Platform** is an end-to-end AI-powered financial analytics application designed to help investors analyze portfolio performance, evaluate financial risk, and receive intelligent investment insights.

The platform integrates **live market data from Finnhub**, **financial news**, **market sentiment analysis**, **portfolio risk metrics**, and an **AI Financial Advisor powered by Google Gemini**.

The application follows a **multi-agent architecture**, where specialized agents perform independent financial analysis before combining their outputs into actionable recommendations presented through an interactive Streamlit dashboard.

## Features

- Portfolio Value Analysis
- Stock Allocation Analysis
- Sector Allocation Analysis
- Volatility Analysis
- Value at Risk (VaR) Calculation
- Sharpe Ratio Computation
- Real-Time Financial News Aggregation
- Sentiment Analysis using TextBlob
- Recommendation Agent
- Chart Generation using Matplotlib
- CSV Report Generation
- MCP Server Integration
- Streamlit Dashboard

---

## 🏗️ System Architecture

```text
                           User
                             │
                             ▼
                  Streamlit Dashboard
                             │
     ┌───────────────────────┼────────────────────────┐
     │                       │                        │
     ▼                       ▼                        ▼
Portfolio Agent        Risk Analysis Agent      AI Advisor Agent
     │                       │                        │
     │                       │                        │
     ▼                       ▼                        ▼
Live Portfolio         VaR + Sharpe Ratio       Google Gemini
     │                       │                        │
     └───────────────┬───────────────┬────────────────┘
                     ▼               ▼
               Financial MCP Server
                     │
         ┌───────────┼────────────┐
         │           │            │
         ▼           ▼            ▼
 Live Prices     Market News   Recommendations
 (Finnhub API)   RSS Feed      Financial Tools
                     │
                     ▼
             Final Financial Insights
```

---

## 🤖 Multi-Agent Workflow

The application follows a modular multi-agent architecture where each agent is responsible for a specific financial task.

### 📊 Portfolio Agent

- Reads portfolio holdings
- Calculates live portfolio value
- Computes allocation percentages

---

### 📉 Risk Analysis Agent

Calculates:

- Portfolio Volatility
- Value at Risk (95%)
- Sharpe Ratio

---

### 📰 News Agent

- Fetches latest financial news
- Monitors market events
- Provides current market context

---

### 😊 Sentiment Agent

Uses **TextBlob** to classify news headlines into:

- Positive
- Neutral
- Negative

---

### 🤖 AI Advisor Agent

Powered by **Google Gemini**.

Combines:

- Portfolio Value
- Sharpe Ratio
- Value at Risk
- Market Sentiment
- Latest News

to generate intelligent investment recommendations.

---

### 🔌 FastMCP Server

The MCP server exposes reusable financial tools including:

- Portfolio Value
- Sharpe Ratio
- Value at Risk
- Market Sentiment
- Latest News
- Investment Recommendation
## MCP Tools

The Financial Risk MCP Server exposes the following tools:

- `get_portfolio_value()`
- `get_sharpe_ratio()`
- `get_var()`
- `get_sentiment()`
- `get_latest_news()`
- `get_recommendation()`

---

## 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.13 |
| Dashboard | Streamlit |
| AI Model | Google Gemini 2.5 Flash |
| MCP Framework | FastMCP |
| Market Data API | Finnhub API |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib |
| NLP | TextBlob |
| News Source | Google News RSS |
| Environment Management | python-dotenv |
| HTTP Requests | Requests |
| Version Control | Git & GitHub |
| Deployment | Streamlit Community Cloud |

---

## 📂 Project Structure

```text
multi-agent-financial-risk-intelligence-platform/
│
├── dashboard/
│   ├── app.py
│   └── components/
│       ├── advisor.py
│       ├── dashboard.py
│       ├── portfolio.py
│       ├── sidebar.py
│       └── __init__.py
│
├── data/
│   └── portfolio.csv
│
├── Charts/
│   ├── portfolio_allocation.png
│   ├── sector_allocation.png
│   └── daily_returns.png
│
├── utils/
│   └── finance.py
│
├── reports/
│
├── llm.py
├── server.py
├── main.py
├── requirements.txt
├── README.md
└── .env
```

## Financial Metrics Implemented

### Value at Risk (VaR)

Measures the maximum expected loss over a given period at a specified confidence level.

```text
VaR = Mean Return - (Z-Score × Standard Deviation)
```

### Sharpe Ratio

Evaluates risk-adjusted returns.

```text
Sharpe Ratio =
(Average Return - Risk Free Rate)
                /
            Volatility
```

### Volatility

Measures the variability of stock returns.

```text
Volatility = Standard Deviation of Daily Returns
```

---

## Folder Structure

```text
multi-agent-financial-risk-intelligence-platform/
|
├── data/
│   └── portfolio.csv
|
├── charts/
│   ├── portfolio_allocation.png
│   ├── sector_allocation.png
│   └── daily_returns.png
|
├── dashboard/
│   └── app.py
|
├── reports/
│   └── report.csv
|
├── main.py
├── server.py
├── README.md
└── requirements.txt
```

---
## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mishtisethi12/multi-agent-financial-risk-intelligence-platform.git

cd multi-agent-financial-risk-intelligence-platform
```

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

FINNHUB_API_KEY=YOUR_FINNHUB_API_KEY
```

> Never commit your `.env` file to GitHub.

---

## ▶️ Running the Project

### Run the Financial Analytics Engine

```bash
python main.py
```

---

### Run the FastMCP Server

```bash
python server.py
```

---

### Launch the Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

Deployment includes:

- Live Streamlit Dashboard
- Google Gemini Integration
- Finnhub API Integration
- FastMCP Financial Server
- AI Financial Advisor

After deployment, update the Live Demo section with your Streamlit URL.

---

## 📊 Financial Metrics

### 📉 Value at Risk (VaR)

Value at Risk estimates the maximum expected portfolio loss over a specified period at a given confidence level.

**Confidence Level:** 95%

---

### 📈 Sharpe Ratio

The Sharpe Ratio measures the risk-adjusted return of the investment portfolio.

Higher values indicate better performance relative to risk.

---

### 📊 Portfolio Allocation

Calculates the percentage contribution of each stock to the total portfolio value.

---

### 🏦 Sector Allocation

Groups investments by sector to evaluate diversification.

---

### 😊 Market Sentiment

Financial news headlines are analyzed using **TextBlob** and classified as:

- Positive
- Neutral
- Negative

---

### 🤖 AI Financial Advisor

Google Gemini combines:

- Portfolio Value
- VaR
- Sharpe Ratio
- Market Sentiment
- Financial News

to generate personalized investment insights.








## Sample Output

| Metric | Value |
|-------|------|
| Portfolio Value | $98,052 |
| Sharpe Ratio | 0.13 |
| Value at Risk | $2,532 |
| Sentiment | Positive |

---
---

# 📸 Screenshots

> Replace these placeholders with actual screenshots after uploading them to the repository.

## Dashboard

```
images/dashboard.png
```

---

## Portfolio Analytics

```
images/portfolio.png
```

---

## AI Financial Advisor

```
images/advisor.png
```

---

## Risk Analytics

```
images/risk.png
```

---

# 🚀 Future Enhancements

- Multi-Portfolio Support
- User Authentication
- Historical Portfolio Performance
- Monte Carlo Risk Simulation
- Portfolio Optimization using Modern Portfolio Theory
- AI-powered Portfolio Rebalancing
- Real-time Market Alerts
- Interactive Stock Comparison Dashboard
- PDF Financial Report Generation
- Docker Deployment
- CI/CD Pipeline using GitHub Actions

---

# 💡 Learning Outcomes

This project demonstrates practical experience with:

- Multi-Agent System Design
- Financial Risk Analytics
- FastMCP Tool Development
- Google Gemini Integration
- Prompt Engineering
- REST API Integration
- Streamlit Dashboard Development
- Portfolio Risk Assessment
- Git & GitHub Workflow
- Cloud Deployment

---

# 👩‍💻 Author

**Mishti Sethi**

AI/ML Undergraduate

Interested in:

- Artificial Intelligence
- Financial Analytics
- Multi-Agent Systems
- Data Analytics
- Machine Learning

GitHub:

https://github.com/mishtisethi12

LinkedIn:

*(Add your LinkedIn profile here)*

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.

## Key Achievements

- Developed an end-to-end financial risk analytics platform.
- Implemented multiple specialized agents for risk assessment and market analysis.
- Integrated MCP (Model Context Protocol) to expose financial tools.
- Leveraged real-time financial data using Yahoo Finance and Google News RSS.
- Built an interactive dashboard for portfolio visualization and monitoring.
- Generated actionable investment recommendations using quantitative and qualitative analysis.

---

## Conclusion

The Multi-Agent Financial Risk Intelligence Platform demonstrates the integration of financial analytics, artificial intelligence, multi-agent systems, and MCP-based tool orchestration to build an intelligent financial risk assessment solution.

The project provides a comprehensive view of portfolio performance by combining quantitative financial metrics with qualitative market intelligence, making it a practical application of AI in the financial domain.
