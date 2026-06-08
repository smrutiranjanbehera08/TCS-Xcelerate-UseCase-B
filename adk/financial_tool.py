import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from financial_agent import get_financial_data


def financial_tool(symbol: str):
    return get_financial_data(symbol)