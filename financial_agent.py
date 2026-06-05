import yfinance as yf

def get_financial_data(symbol):
    ticker = yf.Ticker(symbol)
    info = ticker.info

    return {
        "Company": info.get("longName"),
        "Current Price": info.get("currentPrice"),
        "Market Cap": info.get("marketCap"),
        "PE Ratio": info.get("trailingPE"),
        "Sector": info.get("sector"),
        "Industry": info.get("industry")
    }

if __name__ == "__main__":
    symbol = input("Enter Stock Symbol: ")
    data = get_financial_data(symbol)

    for key, value in data.items():
        print(f"{key}: {value}")