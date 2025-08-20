from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_so_far, max_return = float('inf'), 0.0
    for price in prices:
        min_so_far = min(price, min_so_far)
        current_return = price - min_so_far
        max_return = max(current_return, max_return)
    return max_return


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
