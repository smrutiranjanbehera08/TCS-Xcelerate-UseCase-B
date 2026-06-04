import yfinance as yf

stock = yf.Ticker("RELIANCE.NS")

info = stock.info

print("Company:", info.get("longName"))
print("Market Cap:", info.get("marketCap"))
print("PE Ratio:", info.get("trailingPE"))