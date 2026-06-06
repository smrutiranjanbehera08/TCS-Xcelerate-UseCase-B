from financial_agent import get_financial_data
from news_agent import get_news
from peer_comparison_agent import compare_companies

def get_complete_report(symbol):

    financial_data = get_financial_data(symbol)

    news_data = get_news(symbol)

    peer_data = compare_companies([
        "TCS.NS",
        "INFY.NS",
        "WIPRO.NS"
    ])

    return {
        "financial": financial_data,
        "news": news_data,
        "peer": peer_data
    }


if __name__ == "__main__":

    symbol = input("Enter Stock Symbol: ")

    report = get_complete_report(symbol)

    print("\n===== COMPANY REPORT =====\n")

    for key, value in report["financial"].items():
        print(f"{key}: {value}")

    print("\n===== LATEST NEWS =====\n")

    for i, headline in enumerate(report["news"], start=1):
        print(f"{i}. {headline}")

    print("\n===== PEER COMPARISON =====\n")

    for company in report["peer"]:
        print("Company:", company["Company"])
        print("Current Price:", company["Current Price"])
        print("Market Cap:", company["Market Cap"])
        print("PE Ratio:", company["PE Ratio"])
        print("-" * 40)