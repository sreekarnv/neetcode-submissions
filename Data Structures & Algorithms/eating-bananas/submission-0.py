class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        minval = max(piles)

        while l <= r:
            mid = (l + r) // 2

            total_hrs = 0 
            for p in piles:
                total_hrs += math.ceil(p / mid)
            
            if total_hrs <= h:
                minval = min(mid, minval)
                r = mid - 1
            else:
                l = mid + 1
        
        return minval