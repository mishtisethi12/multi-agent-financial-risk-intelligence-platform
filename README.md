# 📈 Multi-Agent Financial Risk Intelligence Platform

An AI-powered financial analytics platform that leverages **Multi-Agent Systems**, **FastMCP**, **Google Gemini**, **Finnhub API**, and **Streamlit** to perform intelligent portfolio analysis, financial risk assessment, market sentiment analysis, and AI-driven investment recommendations.

The platform combines quantitative financial metrics with real-time market intelligence to help investors better understand portfolio performance and potential financial risks.

---

## 🚀 Live Demo

🔗 ** Streamlit Application**

> https://multi-agent-financial-risk-intelligence-platform-dp6kcy9gcgcdc.streamlit.app/


## ⭐ Key Features

- 📊 Live Portfolio Valuation
- 📈 Portfolio Allocation Analysis
- 🏦 Sector Allocation Analysis
- 📉 Value at Risk (VaR)
- 📊 Sharpe Ratio Calculation
- ⚡ Live Stock Prices using Finnhub API
- 📰 Real-Time Financial News
- 😊 News Sentiment Analysis
- 🤖 AI Financial Advisor using Google Gemini
- 🔌 FastMCP Financial Server
- 📋 CSV Report Generation
- 📊 Interactive Streamlit Dashboard
- ☁️ Cloud Deployment

---

## Dashboard Preview

### Dashboard
![Dashboard](images/dashboard.png)

```

```

---

### Portfolio Analytics


```
![Portfolio Analytics](images/portfolio.png)
```

---

### AI Financial Advisor



```
images/advisor.png
```
![AI Financial Advisor](images/advisor.png)
---

### Risk Analytics

> Add screenshot

```
images/risk.png
```
## Risk Analytics

![Risk Analytics](images/risk.png)
---

# 📌 Project Overview

The **Multi-Agent Financial Risk Intelligence Platform** is an end-to-end financial analytics application designed to simulate an intelligent financial assistant capable of analyzing investment portfolios using multiple specialized AI agents.

The system combines:

- Live Portfolio Valuation
- Portfolio Risk Analysis
- Value at Risk (VaR)
- Sharpe Ratio
- Market Sentiment Analysis
- Financial News Aggregation
- AI-powered Financial Recommendations

into a single interactive dashboard.

Unlike traditional portfolio trackers, this platform follows a **Multi-Agent Architecture**, where individual agents independently perform financial analysis before combining their outputs to generate intelligent recommendations.

---

# 🎯 Objectives

The primary objectives of this project are:

- Build an AI-powered financial analytics platform.
- Demonstrate Multi-Agent System architecture.
- Integrate FastMCP for reusable financial tools.
- Perform portfolio risk assessment.
- Provide AI-generated investment recommendations.
- Visualize financial metrics through an interactive dashboard.
- Deploy a production-ready Streamlit application.

---

# ✨ Highlights

- Multi-Agent Architecture
- FastMCP Financial Server
- Google Gemini Integration
- Finnhub Live Market Data
- Streamlit Interactive Dashboard
- Financial News Aggregation
- Market Sentiment Analysis
- Portfolio Allocation Visualization
- Sector Allocation Visualization
- Value at Risk (95%)
- Sharpe Ratio
- Cloud Deployment
  ---

# 🏗️ System Architecture

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
                     ▼
             FastMCP Financial Server
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 Finnhub API     News Agent     Recommendation
 Live Prices      RSS Feed          Engine
                     │
                     ▼
             Final Financial Insights
```

---

# 🤖 Multi-Agent Workflow

The application follows a modular **Multi-Agent Architecture**, where every agent performs a dedicated financial task before contributing to the final investment recommendation.

---

## 📊 Portfolio Agent

Responsible for:

- Reading portfolio holdings
- Calculating live portfolio value
- Computing stock allocation
- Computing sector allocation

---

## 📉 Risk Analysis Agent

Calculates important financial risk metrics including:

- Portfolio Volatility
- Value at Risk (95%)
- Sharpe Ratio

These metrics help estimate portfolio performance and downside risk.

---

## 📰 News Agent

Collects the latest financial news from reliable RSS feeds.

Responsibilities include:

- Market updates
- Company news
- Economic events
- Financial headlines

---

## 😊 Sentiment Agent

Performs sentiment analysis on financial news using **TextBlob**.

Each news headline is classified as:

- 🟢 Positive
- 🟡 Neutral
- 🔴 Negative

This helps estimate current market sentiment.

---

## 🤖 AI Financial Advisor

Powered by **Google Gemini 2.5 Flash**.

The AI combines:

- Portfolio Value
- Sharpe Ratio
- Value at Risk
- Market Sentiment
- Financial News

to answer investor questions and generate personalized financial recommendations.

---

## 🔌 FastMCP Financial Server

The project exposes reusable financial tools using **FastMCP**.

Available tools include:

- Portfolio Value
- Sharpe Ratio
- Value at Risk
- Latest News
- Market Sentiment
- Investment Recommendation

The MCP server enables AI models to access financial information through structured tool calls.

---

# 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.13 |
| Dashboard | Streamlit |
| AI Model | Google Gemini 2.5 Flash |
| MCP Framework | FastMCP |
| Market Data | Finnhub API |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib |
| Natural Language Processing | TextBlob |
| Financial News | Google News RSS |
| Environment Variables | python-dotenv |
| Version Control | Git & GitHub |
| Deployment | Streamlit Community Cloud |

---

# 🔧 MCP Tools

The Financial Risk MCP Server exposes the following tools:

| Tool | Description |
|------|-------------|
| `get_portfolio_value()` | Calculates current portfolio value |
| `get_sharpe_ratio()` | Returns portfolio Sharpe Ratio |
| `get_var()` | Computes Value at Risk (95%) |
| `get_sentiment()` | Returns current market sentiment |
| `get_latest_news()` | Retrieves latest financial news |
| `get_recommendation()` | Generates investment recommendation |

---
# 📂 Project Structure

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
├── Charts/
│   ├── portfolio_allocation.png
│   ├── sector_allocation.png
│   └── daily_returns.png
│
├── data/
│   └── portfolio.csv
│
├── reports/
│   └── report.csv
│
├── utils/
│   └── finance.py
│
├── llm.py
├── server.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/mishtisethi12/multi-agent-financial-risk-intelligence-platform.git

cd multi-agent-financial-risk-intelligence-platform
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

FINNHUB_API_KEY=YOUR_FINNHUB_API_KEY
```

> **Important:** Never commit your `.env` file to GitHub.

---

# ▶️ Running the Project

## Run the Analytics Engine

```bash
python main.py
```

---

## Start the FastMCP Server

```bash
python server.py
```

---

## Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

---

# ☁️ Deployment

The application is deployed on **Streamlit Community Cloud**.

Deployment includes:

- Google Gemini API
- Finnhub API
- FastMCP Financial Server
- AI Financial Advisor
- Interactive Dashboard

To deploy:

1. Push the repository to GitHub.
2. Connect the repository with Streamlit Community Cloud.
3. Add the required API keys in **Secrets**:

```toml
GEMINI_API_KEY="YOUR_KEY"

FINNHUB_API_KEY="YOUR_KEY"
```

4. Deploy the application.

---

# 📈 Dashboard Features

The Streamlit dashboard provides:

- Live Portfolio Value
- Portfolio Allocation Chart
- Sector Allocation Chart
- Daily Returns Visualization
- Value at Risk
- Sharpe Ratio
- Market Sentiment
- AI Financial Advisor
- Financial News
- MCP Server Status

---

# 📊 Financial Metrics

## Value at Risk (VaR)

Value at Risk estimates the potential portfolio loss over a specified time period at a chosen confidence level.

Confidence Level:

**95%**

---

## Sharpe Ratio

Measures portfolio performance after adjusting for risk.

Higher values indicate better risk-adjusted returns.

---

## Portfolio Allocation

Calculates each stock's contribution to the overall portfolio value.

---

## Sector Allocation

Groups holdings into sectors to measure diversification.

---

## Market Sentiment

Financial headlines are analyzed using **TextBlob** and classified into:

- Positive
- Neutral
- Negative

---

## AI Financial Advisor

Google Gemini analyzes:

- Portfolio Value
- Portfolio Risk
- Sharpe Ratio
- VaR
- Market Sentiment
- Latest Financial News

to generate personalized investment recommendations.

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

The platform is designed with scalability in mind. Planned enhancements include:

- Multi-Portfolio Support
- User Authentication & Secure Login
- Historical Portfolio Performance Tracking
- Portfolio Optimization using Modern Portfolio Theory (MPT)
- Monte Carlo Risk Simulation
- Real-Time Market Alerts
- Interactive Stock Comparison Dashboard
- PDF Financial Report Generation
- Watchlist Management
- Docker Containerization
- CI/CD Pipeline with GitHub Actions
- Database Integration (PostgreSQL/MongoDB)
- Role-Based User Access
- Advanced Risk Metrics (Beta, Alpha, Sortino Ratio)

---

# 💡 Learning Outcomes

This project provided hands-on experience with:

- Multi-Agent System Design
- Financial Risk Analytics
- Portfolio Analysis
- FastMCP Tool Development
- Google Gemini API Integration
- Prompt Engineering
- REST API Integration
- Streamlit Dashboard Development
- Financial Data Visualization
- Git & GitHub Workflow
- Cloud Deployment
- Environment Variable Management
- Modular Python Application Development

---

# 🎯 Key Achievements

- Designed and developed an end-to-end AI-powered financial analytics platform.
- Implemented a modular Multi-Agent architecture for portfolio analysis and financial decision support.
- Built reusable financial tools using FastMCP.
- Integrated Google Gemini to provide intelligent financial insights through a conversational AI advisor.
- Connected the application with Finnhub API to retrieve live market data.
- Performed portfolio risk analysis using Value at Risk (VaR) and Sharpe Ratio.
- Visualized portfolio allocation, sector allocation, and daily returns using interactive charts.
- Deployed the application on Streamlit Community Cloud.

---

# 🌟 Why This Project?

Traditional portfolio trackers primarily display numbers without explaining investment decisions.

This project goes a step further by combining:

- Financial Analytics
- Artificial Intelligence
- Multi-Agent Systems
- Financial APIs
- Cloud Deployment

to create an intelligent financial assistant capable of delivering actionable portfolio insights.

---

# 👩‍💻 Author

## Mishti Sethi

AI/ML Undergraduate

Passionate about:

- Artificial Intelligence
- Financial Analytics
- Multi-Agent Systems
- Machine Learning
- Data Analytics
- FinTech

### GitHub

https://github.com/mishtisethi12

### LinkedIn

Add your LinkedIn profile here

---

# 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

---

# ⭐ Support

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub.

It really helps and motivates future development.

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project in accordance with the license terms.

---

# 🙏 Acknowledgements

This project makes use of the following technologies and services:

- Google Gemini API
- Finnhub API
- FastMCP
- Streamlit
- Pandas
- NumPy
- Matplotlib
- TextBlob
- Python

---

## Thank you for visiting this repository!

If you enjoyed exploring this project, don't forget to ⭐ the repository and connect with me on GitHub.
