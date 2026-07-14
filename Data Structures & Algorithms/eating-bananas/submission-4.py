class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpd = float("inf")
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2

            th = 0
            for p in piles:
                th += math.ceil(p / mid)

            if th <= h:
                minSpd = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return minSpd