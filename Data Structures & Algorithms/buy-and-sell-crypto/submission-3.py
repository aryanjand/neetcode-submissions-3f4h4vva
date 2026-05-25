import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = max(prices)

        for stock in prices:
            buy = min(stock, buy)
            res = max(res, stock - buy)

        return res