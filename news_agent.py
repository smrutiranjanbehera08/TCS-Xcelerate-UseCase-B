import yfinance as yf

def get_news(symbol):
    ticker = yf.Ticker(symbol)
    news = ticker.news

    headlines = []

    for article in news[:5]:
        headlines.append(article["content"]["title"])

    return headlines

if __name__ == "__main__":
    symbol = input("Enter Stock Symbol: ")

    for news in get_news(symbol):
        print(news)