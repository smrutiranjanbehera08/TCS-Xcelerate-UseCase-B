from news_tool import news_tool

result = news_tool("TCS.NS")

for i, news in enumerate(result, start=1):
    print(f"{i}. {news}")