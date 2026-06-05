import yfinance as yf

symbol = input("Enter Stock Symbol: ")

ticker = yf.Ticker(symbol)

info = ticker.info

print("\n===== COMPANY REPORT =====")
print("Company:", info.get("longName"))
print("Current Price:", info.get("currentPrice"))
print("Market Cap:", info.get("marketCap"))
print("PE Ratio:", info.get("trailingPE"))
print("Sector:", info.get("sector"))
print("Industry:", info.get("industry"))
print("52 Week High:", info.get("fiftyTwoWeekHigh"))
print("52 Week Low:", info.get("fiftyTwoWeekLow"))