import yfinance as yf
import pandas as pd
import numpy as np

sector_map = {
    "AAPL": "Technology",
    "MSFT": "Technology",
    "NVDA": "Technology",
    "GOOGL": "Technology",
    "AMZN": "Consumer",
    "META": "Technology",
    "JPM": "Finance",
    "GS": "Finance",
    "TSLA": "Automotive",
    "NFLX": "Entertainment"
}


def analyze_portfolio():
    portfolio = pd.read_csv("data/portfolio.csv")

    total_value = 0
    stock_values = []

    for _, row in portfolio.iterrows():
        ticker = row["Ticker"]
        shares = row["Shares"]

        stock = yf.Ticker(ticker)
        price = stock.fast_info.get("lastPrice")

        if price is None:
            continue

        value = price * shares
        total_value += value
        stock_values.append((ticker, value))

    return total_value, stock_values


def calculate_var(total_value):
    hist = yf.Ticker("AAPL").history(period="1y")
    hist["Daily Return"] = hist["Close"].pct_change()

    volatility = hist["Daily Return"].std()
    z_score = 1.65

    var = total_value * volatility * z_score

    return round(var, 2), volatility


def calculate_sharpe(volatility):
    hist = yf.Ticker("AAPL").history(period="1y")
    hist["Daily Return"] = hist["Close"].pct_change()

    risk_free_rate = 0.02 / 252
    average_return = hist["Daily Return"].mean()

    sharpe = (average_return - risk_free_rate) / volatility

    return round(sharpe, 2)