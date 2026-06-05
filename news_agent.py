import yfinance as yf

symbol = input("Enter Stock Symbol: ")

ticker = yf.Ticker(symbol)

news = ticker.news

print("\n===== LATEST NEWS =====\n")

for i, article in enumerate(news[:5], start=1):
    print(f"{i}. {article['content']['title']}")