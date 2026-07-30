import csv
import matplotlib.pyplot as plt
from textblob import TextBlob
import feedparser
import numpy as np
import pandas as pd
import yfinance as yf

# -------------------------------------
# LOAD PORTFOLIO
# -------------------------------------

portfolio = pd.read_csv("data/portfolio.csv")

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

# -------------------------------------
# PORTFOLIO ANALYSIS
# -------------------------------------

total_value = 0
stock_values = []
sector_values = {}

for index, row in portfolio.iterrows():

    ticker = row["Ticker"]
    shares = row["Shares"]

    print(f"\nFetching data for: {ticker}")

    stock = yf.Ticker(ticker)

    # Fetch latest stock price
    price = stock.fast_info.get("lastPrice")

    if price is None:
        print(f"Could not fetch price for {ticker}")
        continue

    value = price * shares

    total_value += value

    stock_values.append((ticker, value))

    sector = sector_map[ticker]

    if sector not in sector_values:
        sector_values[sector] = 0

    sector_values[sector] += value

    print(f"{ticker}: ${price:.2f}")
    print(f"Shares: {shares}")
    print(f"Value: ${value:.2f}")
    print("-" * 30)

# -------------------------------------
# TOTAL PORTFOLIO VALUE
# -------------------------------------

print("\nTotal Portfolio Value:")
print(f"${total_value:.2f}")

# -------------------------------------
# PORTFOLIO ALLOCATION
# -------------------------------------

print("\nPortfolio Allocation:")

for ticker, value in stock_values:

    allocation = (value / total_value) * 100

    print(f"{ticker}: {allocation:.2f}%")
#PIECHART
labels = [ticker for ticker, value in stock_values]
sizes = [value for ticker, value in stock_values]

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Portfolio Allocation")
plt.savefig("Charts/portfolio_allocation.png")
plt.close()

# -------------------------------------
# SECTOR ALLOCATION
# -------------------------------------

print("\nSector Allocation:")

for sector, value in sector_values.items():

    allocation = (value / total_value) * 100

    print(f"{sector}: {allocation:.2f}%")
#SECTOR PIECHART
plt.figure(figsize=(8, 8))

plt.pie(
    sector_values.values(),
    labels=sector_values.keys(),
    autopct='%1.1f%%'
)

plt.title("Sector Allocation")
plt.savefig("charts/sector_allocation.png")
plt.close()

# -------------------------------------
# VOLATILITY ANALYSIS
# -------------------------------------

print("\n" + "=" * 30)
print("VOLATILITY ANALYSIS")
print("=" * 30)

aapl = yf.Ticker("AAPL")

hist = aapl.history(period="1y")

hist["Daily Return"] = hist["Close"].pct_change()

volatility = hist["Daily Return"].std()

print(f"\nApple Volatility: {volatility * 100:.2f}%")
print("Stock Analyzed: AAPL")

if volatility < 0.01:
    print("Risk Level: Low")

elif volatility < 0.02:
    print("Risk Level: Moderate")

else:
    print("Risk Level: High")
    
#----------------------
#DAILY RETURN
#----------------------
plt.figure(figsize=(10, 5))

plt.plot(hist.index, hist["Daily Return"])

plt.title("Apple Daily Returns")
plt.xlabel("Date")
plt.ylabel("Daily Return")

plt.savefig("charts/daily_returns.png")
plt.close()

# -------------------------------------
# VALUE AT RISK (VaR)
# -------------------------------------

print("\n" + "=" * 30)
print("VALUE AT RISK (VaR)")
print("=" * 30)

z_score = 1.65

var = total_value * volatility * z_score

print(f"Portfolio Value: ${total_value:.2f}")
print("Confidence Level: 95%")
print(f"Value at Risk: ${var:.2f}")

print(
    f"\nInterpretation: There is a 95% confidence "
    f"that the portfolio will not lose more than ${var:.2f} in a day."
)
#------------------------------
#Sharpe ratio
#------------------------------
print("\n" + "=" * 30)
print("SHARPE RATIO")
print("=" * 30)

risk_free_rate = 0.02 / 252

average_return = hist["Daily Return"].mean()

sharpe_ratio = (average_return - risk_free_rate) / volatility

print(f"Average Daily Return: {average_return*100:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

if sharpe_ratio < 1:
    print("Performance: Poor")
elif sharpe_ratio < 2:
    print("Performance: Good")
elif sharpe_ratio < 3:
    print("Performance: Very Good")
else:
    print("Performance: Excellent")
#-------------------------------
#NEWS AGENT
#-------------------------------
print("\n" + "=" * 30)
print("NEWS AGENT")
print("=" * 30)

ticker = "TSLA"

url = f"https://news.google.com/rss/search?q={ticker}"

feed = feedparser.parse(url)

print(f"Latest News for {ticker}:\n")

for entry in feed.entries[:5]:
    print("-", entry.title)
#------------------------------
#SENTIMENT AGENT
#------------------------------
print("\n" + "=" * 30)
print("SENTIMENT AGENT")
print("=" * 30)

positive = 0
negative = 0
neutral = 0

for entry in feed.entries[:5]:

    headline = entry.title

    sentiment = TextBlob(headline).sentiment.polarity

    if sentiment > 0:
        label = "Positive"
        positive += 1

    elif sentiment < 0:
        label = "Negative"
        negative += 1

    else:
        label = "Neutral"
        neutral += 1

    print(f"{headline}")
    print(f"Sentiment Score: {sentiment:.2f}")
    print(f"Label: {label}")
    print("-" * 30)
    
    print("\nOVERALL SENTIMENT")

if positive > negative:
    print("Overall Sentiment: POSITIVE")

elif negative > positive:
    print("Overall Sentiment: NEGATIVE")

else:
    print("Overall Sentiment: NEUTRAL")
#-----------------------------------
#RECOMMENDATION SYSTEM
#----------------------------------
print("\n" + "=" * 30)
print("RECOMMENDATION AGENT")
print("=" * 30)

if negative > positive and sharpe_ratio < 1:

    print("Recommendation:")
    print("- Consider reducing TSLA exposure.")
    print("- Review portfolio diversification.")
    print("- Monitor upcoming earnings reports.")

elif sharpe_ratio >= 1:

    print("Recommendation:")
    print("- Portfolio performance is acceptable.")
    print("- Continue monitoring market conditions.")

else:

    print("Recommendation:")
    print("- Hold current positions.")
    print("- Gather more market data.")
    
import matplotlib.pyplot as plt

tickers = [ticker for ticker, value in stock_values]
values = [value for ticker, value in stock_values]

plt.figure(figsize=(8,5))
plt.bar(tickers, values)
plt.title("Portfolio Allocation")
plt.xlabel("Stocks")
plt.ylabel("Value ($)")

plt.savefig("portfolio_chart.png")
plt.show()

print("\n" + "=" * 30)
print("GENERATING CSV REPORT")
print("=" * 30)

with open("report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Ticker", "Value", "Allocation (%)"])

    for ticker, value in stock_values:
        allocation = (value / total_value) * 100
        writer.writerow([ticker, round(value, 2), round(allocation, 2)])

print("CSV Report saved as report.csv")