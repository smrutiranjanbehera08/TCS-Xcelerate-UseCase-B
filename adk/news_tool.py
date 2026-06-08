import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from news_agent import get_news


def news_tool(symbol: str):
    return get_news(symbol)