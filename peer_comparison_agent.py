import yfinance as yf

company1 = input("Enter Company 1 Symbol: ")
company2 = input("Enter Company 2 Symbol: ")
company3 = input("Enter Company 3 Symbol: ")

companies = [company1, company2, company3]

print("\n===== PEER COMPARISON REPORT =====\n")

for symbol in companies:
    ticker = yf.Ticker(symbol)
    info = ticker.info

    print("Company:", info.get("longName"))
    print("Current Price:", info.get("currentPrice"))
    print("Market Cap:", info.get("marketCap"))
    print("PE Ratio:", info.get("trailingPE"))
    print("-" * 40)