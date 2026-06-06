import yfinance as yf

def get_filing_summary(symbol):
    ticker = yf.Ticker(symbol)
    info = ticker.info

    return {
        "Company": info.get("longName"),
        "Business Summary": info.get("longBusinessSummary"),
        "Employees": info.get("fullTimeEmployees"),
        "Website": info.get("website")
    }

if __name__ == "__main__":
    symbol = input("Enter Stock Symbol: ")
    
    filing = get_filing_summary(symbol)

    print("\n===== FILINGS SUMMARY =====\n")
    print("Company:", filing["Company"])
    print("Employees:", filing["Employees"])
    print("Website:", filing["Website"])
    print("\nBusiness Summary:\n")
    print(filing["Business Summary"])