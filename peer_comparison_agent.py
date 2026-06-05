import yfinance as yf

companies = {
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "Wipro": "WIPRO.NS"
}

print("\n===== PEER COMPARISON REPORT =====\n")

for company, symbol in companies.items():
    ticker = yf.Ticker(symbol)
    info = ticker.info

    print("Company:", company)
    print("Current Price:", info.get("currentPrice"))
    print("Market Cap:", info.get("marketCap"))
    print("PE Ratio:", info.get("trailingPE"))
    print("-" * 40)