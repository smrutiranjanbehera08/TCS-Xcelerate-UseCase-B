from coordinator_agent import get_complete_report

def generate_report(symbol):

    report = get_complete_report(symbol)

    financial = report["financial"]
    news = report["news"]
    peers = report["peer"]

    report_text = ""

    report_text += "===== INVESTMENT RESEARCH REPORT =====\n\n"

    report_text += f"Company: {financial['Company']}\n"
    report_text += f"Sector: {financial['Sector']}\n"
    report_text += f"Industry: {financial['Industry']}\n\n"

    report_text += "----- Financial Summary -----\n"
    report_text += f"Current Price: {financial['Current Price']}\n"
    report_text += f"Market Cap: {financial['Market Cap']}\n"
    report_text += f"PE Ratio: {financial['PE Ratio']}\n\n"

    report_text += "----- Latest News -----\n"
    for i, headline in enumerate(news, start=1):
        report_text += f"{i}. {headline}\n"

    report_text += "\n----- Peer Comparison -----\n"
    for company in peers:
        report_text += (
            f"{company['Company']} | "
            f"Price: {company['Current Price']} | "
            f"PE: {company['PE Ratio']}\n"
        )

    report_text += "\n----- Conclusion -----\n"
    report_text += (
        f"{financial['Company']} operates in the "
        f"{financial['Sector']} sector. "
        "Investors should review financial metrics, "
        "latest news, and peer performance before making decisions.\n"
    )

    print(report_text)

    filename = f"report_{symbol.replace('.','_')}.txt"

    with open(filename, "w") as file:
        file.write(report_text)

    print(f"\nReport saved as: {filename}")


if __name__ == "__main__":
    symbol = input("Enter Stock Symbol: ")
    generate_report(symbol)