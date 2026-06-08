from financial_agent import get_financial_data
from news_agent import get_news
from peer_comparison_agent import compare_companies, get_peers
from filings_agent import get_filing_summary


def get_complete_report(symbol):

    financial_data = get_financial_data(symbol)

    news_data = get_news(symbol)

    filing_data = get_filing_summary(symbol)

    peer_data = compare_companies(
    get_peers(symbol)
    )

    return {
        "financial": financial_data,
        "news": news_data,
        "filing": filing_data,
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

    print("\n===== FILINGS SUMMARY =====\n")

    print("Company:", report["filing"]["Company"])
    print("Employees:", report["filing"]["Employees"])
    print("Website:", report["filing"]["Website"])

    print("\nBusiness Summary:\n")

    summary = report["filing"]["Business Summary"]

    if summary:
        print(summary[:800] + "...")
    else:
        print("No business summary available.")

    print("\n===== PEER COMPARISON =====\n")

    for company in report["peer"]:
        print("Company:", company["Company"])
        print("Current Price:", company["Current Price"])
        print("Market Cap:", company["Market Cap"])
        print("PE Ratio:", company["PE Ratio"])
        print("-" * 40)