class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = left = 0

        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            
            maxProfit = max(maxProfit, profit)

        return maxProfit