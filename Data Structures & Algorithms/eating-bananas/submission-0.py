class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        speed = max(piles)

        while l <= r:
            mid = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            
            if hours > h:
                l = mid + 1
            else:
                speed = min(mid, speed)
                r = mid - 1
        
        return speed

