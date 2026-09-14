class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        for r, p in enumerate(prices):
            profit = max(profit, p - prices[l])

            if prices[l] > p:
                l = r

        return profit