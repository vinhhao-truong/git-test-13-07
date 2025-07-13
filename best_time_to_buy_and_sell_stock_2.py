from typing import List


def calProfit(prices: List[int], idx, base: int = -1) -> List[int]:
    if len(prices) == 1:
        return [idx, prices[0] - base]
    idx += 1
    if prices[0] > prices[1]:
        return calProfit([prices[0]], idx, base)
    if base == -1:
        return calProfit(prices[1:], idx, prices[0])
    return calProfit(prices[1:], idx, base)


def maxProfit(prices: List[int]) -> int:
    idx = 0
    profit = 0

    while (idx < len(prices) - 1):
        if prices[idx] < prices[idx + 1]:
            calculate = calProfit(prices[idx:], idx)
            idx = calculate[0]
            profit += calculate[1]
        else:
            idx += 1

    return profit


print(maxProfit([7, 1, 5, 8, 23, 3, 6, 4]))
