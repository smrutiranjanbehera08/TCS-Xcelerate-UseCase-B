import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from filings_agent import get_filing_summary


def filings_tool(symbol: str):
    return get_filing_summary(symbol)