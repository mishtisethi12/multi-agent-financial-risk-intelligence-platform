# Multi-Agent Financial Risk Intelligence Platform

## Overview

The Multi-Agent Financial Risk Intelligence Platform is an AI-powered financial analytics system designed to provide portfolio insights, risk assessment, market sentiment analysis, and investment recommendations. The platform leverages real-time financial data, MCP (Model Context Protocol), and multiple specialized agents to simulate an intelligent financial assistant.

The system combines quantitative risk metrics such as Value at Risk (VaR) and Sharpe Ratio with qualitative insights from real-time financial news and sentiment analysis to deliver actionable recommendations.

---

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

## Project Architecture

```text
                    User
                      |
                      v
            Streamlit Dashboard
                      |
                      v
       Multi-Agent Financial System
                      |
    ------------------------------------------------
    |              |              |               |
Portfolio      Risk Agent     News Agent    MCP Server
 Agent             |               |              |
    |               |               |              |
    |           VaR Agent      Sentiment Agent     |
    |               |               |              |
    ------------------------------------------------
                      |
                      v
            Recommendation Agent
                      |
                      v
               Final Risk Report
```

---

## Multi-Agent Workflow

```text
Portfolio CSV
      |
      v
Portfolio Analysis
      |
      v
Volatility Analysis
      |
      v
Value at Risk (VaR)
      |
      v
Sharpe Ratio
      |
      v
News Agent
      |
      v
Sentiment Agent
      |
      v
Recommendation Agent
      |
      v
CSV Report + Dashboard
```

---

## MCP Tools

The Financial Risk MCP Server exposes the following tools:

- `get_portfolio_value()`
- `get_sharpe_ratio()`
- `get_var()`
- `get_sentiment()`
- `get_latest_news()`
- `get_recommendation()`

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Financial Data | yFinance |
| NLP | TextBlob |
| Visualization | Matplotlib |
| Dashboard | Streamlit |
| MCP | FastMCP |
| News Source | Google News RSS |
| Reporting | CSV |

---

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

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/multi-agent-financial-risk-intelligence-platform.git

cd multi-agent-financial-risk-intelligence-platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Run Portfolio Analytics

```bash
python main.py
```

### Run MCP Server

```bash
python server.py
```

### Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Sample Output

| Metric | Value |
|-------|------|
| Portfolio Value | $98,052 |
| Sharpe Ratio | 0.13 |
| Value at Risk | $2,532 |
| Sentiment | Positive |

---

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
