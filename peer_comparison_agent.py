import yfinance as yf

def compare_companies(company_symbols):

    comparison_data = []

    for symbol in company_symbols:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        comparison_data.append({
            "Company": info.get("longName"),
            "Current Price": info.get("currentPrice"),
            "Market Cap": info.get("marketCap"),
            "PE Ratio": info.get("trailingPE")
        })

    return comparison_data


if __name__ == "__main__":

    company1 = input("Enter Company 1 Symbol: ")
    company2 = input("Enter Company 2 Symbol: ")
    company3 = input("Enter Company 3 Symbol: ")

    companies = [company1, company2, company3]

    result = compare_companies(companies)

    print("\n===== PEER COMPARISON REPORT =====\n")

    for company in result:
        print("Company:", company["Company"])
        print("Current Price:", company["Current Price"])
        print("Market Cap:", company["Market Cap"])
        print("PE Ratio:", company["PE Ratio"])
        print("-" * 40)