import sys


def maxProfit(list: list[int]) -> int:
    profit = 0
    for i in range(0, list):
        profit = max(profit, list[i] - max(list, key=lambda x: (x.split()[i:])))
    return profit


# 책 풀이
def max_profit(prices: list[int]) -> int:
    profit = 0;
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit
