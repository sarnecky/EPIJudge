from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_profits = [0.0] * len(prices)
    for i, price in enumerate(prices): # forward phase, each day has a profit if we sell on that day
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_profits[i] = max_total_profit

    max_profit_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_profit_so_far = max(max_profit_so_far, price)
        max_total_profit = max(max_total_profit, first_buy_profits[i] + max_profit_so_far - price)
    return max_total_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
