class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        r = 0

        while r < len(prices):
            curr = prices[r] - prices[l]
            profit = max(curr, profit)

            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return profit