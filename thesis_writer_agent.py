from coordinator_agent import get_complete_report

def generate_thesis(symbol):

    report = get_complete_report(symbol)

    financial = report["financial"]
    news = report["news"]
    peers = report["peer"]
    filing = report["filing"]

    thesis_text = ""

    thesis_text += "===== INVESTMENT THESIS REPORT =====\n\n"

    thesis_text += f"Company: {financial['Company']}\n"
    thesis_text += f"Sector: {financial['Sector']}\n"
    thesis_text += f"Industry: {financial['Industry']}\n\n"

    thesis_text += "----- Financial Summary -----\n"
    thesis_text += f"Current Price: {financial['Current Price']}\n"
    thesis_text += f"Market Cap: {financial['Market Cap']}\n"
    thesis_text += f"PE Ratio: {financial['PE Ratio']}\n\n"

    thesis_text += "----- Latest News -----\n"
    for i, headline in enumerate(news, start=1):
        thesis_text += f"{i}. {headline}\n"

    thesis_text += "\n----- Business Overview -----\n"
    thesis_text += f"Employees: {filing['Employees']}\n"
    thesis_text += f"Website: {filing['Website']}\n\n"

    summary = filing["Business Summary"]

    if summary:
        thesis_text += summary[:1000] + "...\n"
    else:
        thesis_text += "Business summary not available.\n"

    thesis_text += "\n----- Peer Comparison -----\n"

    for company in peers:
        thesis_text += (
            f"{company['Company']} | "
            f"Price: {company['Current Price']} | "
            f"PE: {company['PE Ratio']}\n"
        )

    thesis_text += "\n----- Bull Case -----\n"

    thesis_text += (
        f"{financial['Company']} is a major player in the "
        f"{financial['Sector']} sector with strong market presence "
        "and established business operations.\n"
    )

    thesis_text += "\n----- Bear Case -----\n"

    thesis_text += (
        "Market volatility, sector competition, and economic "
        "slowdowns may impact future growth and profitability.\n"
    )

    thesis_text += "\n----- Risks -----\n"

    thesis_text += (
        "Investors should consider valuation levels, industry trends, "
        "regulatory changes, and company-specific execution risks.\n"
    )

    thesis_text += "\n----- Investment Thesis -----\n"

    thesis_text += (
        f"{financial['Company']} operates in the "
        f"{financial['Sector']} sector. Based on available financial "
        "data, recent news, company profile, and peer comparison, "
        "investors should perform further due diligence before "
        "making investment decisions.\n"
    )

    print(thesis_text)

    filename = f"thesis_{symbol.replace('.','_')}.txt"

    with open(filename, "w") as file:
        file.write(thesis_text)

    print(f"\nThesis saved as: {filename}")


if __name__ == "__main__":
    symbol = input("Enter Stock Symbol: ")
    generate_thesis(symbol)