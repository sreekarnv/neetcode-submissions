class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        for r in range(len(prices)):
            profit = max(prices[r] - prices[l], profit)

            if prices[r] < prices[l]:
                l = r
        
        return profit