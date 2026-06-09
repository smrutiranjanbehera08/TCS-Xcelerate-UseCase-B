import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from peer_comparison_agent import compare_companies, get_peers


def peer_tool(symbol: str):
    peers = get_peers(symbol)
    return compare_companies(peers)