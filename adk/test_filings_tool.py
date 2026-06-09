from filings_tool import filings_tool

result = filings_tool("TCS.NS")

print("Company:", result["Company"])
print("Employees:", result["Employees"])
print("Website:", result["Website"])

print("\nBusiness Summary:\n")

summary = result["Business Summary"]

if summary:
    print(summary[:500] + "...")
else:
    print("No summary available.")