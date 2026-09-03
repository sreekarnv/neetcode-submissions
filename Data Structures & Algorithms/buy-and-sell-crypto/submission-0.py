class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        for r in range(len(prices)):
            profit = max(profit, prices[r] - prices[l])

            if prices[l] > prices[r]:
                l = r
        
        return profit