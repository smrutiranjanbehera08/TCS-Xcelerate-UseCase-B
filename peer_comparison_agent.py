import yfinance as yf

PEER_MAP = {
    "TCS.NS": ["TCS.NS", "INFY.NS", "WIPRO.NS"],
    "INFY.NS": ["INFY.NS", "TCS.NS", "WIPRO.NS"],
    "WIPRO.NS": ["WIPRO.NS", "TCS.NS", "INFY.NS"],

    "HDFCBANK.NS": ["HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS"],
    "ICICIBANK.NS": ["ICICIBANK.NS", "HDFCBANK.NS", "SBIN.NS"],
    "SBIN.NS": ["SBIN.NS", "HDFCBANK.NS", "ICICIBANK.NS"],

    "RELIANCE.NS": ["RELIANCE.NS", "ONGC.NS", "BPCL.NS"],

    "BHARTIARTL.NS": ["BHARTIARTL.NS", "IDEA.NS", "RELIANCE.NS"],

    "ITC.NS": ["ITC.NS", "HINDUNILVR.NS", "NESTLEIND.NS"],

    "LT.NS": ["LT.NS", "SIEMENS.NS", "ABB.NS"]
}


def get_peers(symbol):
    return PEER_MAP.get(
        symbol.upper(),
        ["TCS.NS", "INFY.NS", "WIPRO.NS"]
    )


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

    symbol = input("Enter Stock Symbol: ")

    peers = get_peers(symbol)

    result = compare_companies(peers)

    print("\n===== PEER COMPARISON REPORT =====\n")

    for company in result:
        print("Company:", company["Company"])
        print("Current Price:", company["Current Price"])
        print("Market Cap:", company["Market Cap"])
        print("PE Ratio:", company["PE Ratio"])
        print("-" * 40)