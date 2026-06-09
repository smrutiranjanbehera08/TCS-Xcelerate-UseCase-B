from coordinator_tool import coordinator_tool

report = coordinator_tool("TCS.NS")

print("\n===== ADK COORDINATOR REPORT =====\n")

print("Company:")
print(report["financial"]["Company"])

print("\nSector:")
print(report["financial"]["Sector"])

print("\nLatest News:")

for news in report["news"][:3]:
    print("-", news)

print("\nPeer Companies:")

for company in report["peers"]:
    print(company["Company"])