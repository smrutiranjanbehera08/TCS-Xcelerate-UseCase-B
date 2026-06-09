from peer_tool import peer_tool

result = peer_tool("HDFCBANK.NS")

for company in result:
    print("Company:", company["Company"])
    print("Current Price:", company["Current Price"])
    print("PE Ratio:", company["PE Ratio"])
    print("-" * 40)