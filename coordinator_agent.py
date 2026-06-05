from financial_agent import get_financial_data
from news_agent import get_news
from peer_comparison_agent import compare_companies

symbol = input("Enter Stock Symbol: ")

financial_data = get_financial_data(symbol)

news_data = get_news(symbol)

peer_data = compare_companies([
    "TCS.NS",
    "INFY.NS",
    "WIPRO.NS"
])

print("\n===== COMPANY REPORT =====\n")

for key, value in financial_data.items():
    print(f"{key}: {value}")

print("\n===== LATEST NEWS =====\n")

for i, headline in enumerate(news_data, start=1):
    print(f"{i}. {headline}")

print("\n===== PEER COMPARISON =====\n")

for company in peer_data:
    print("Company:", company["Company"])
    print("Current Price:", company["Current Price"])
    print("Market Cap:", company["Market Cap"])
    print("PE Ratio:", company["PE Ratio"])
    print("-" * 40)