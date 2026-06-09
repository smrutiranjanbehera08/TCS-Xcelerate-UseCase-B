from financial_tool import financial_tool
from news_tool import news_tool
from filings_tool import filings_tool
from peer_tool import peer_tool


def coordinator_tool(symbol: str):

    financial = financial_tool(symbol)

    news = news_tool(symbol)

    filings = filings_tool(symbol)

    peers = peer_tool(symbol)

    return {
        "financial": financial,
        "news": news,
        "filings": filings,
        "peers": peers
    }