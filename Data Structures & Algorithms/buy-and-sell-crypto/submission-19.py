class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        for r, p in enumerate(prices):
            profit = max(p - prices[l], profit)

            if p < prices[l]:
                l = r
        
        return profit
