class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        capacity = r

        while l < r:
            mid = (l + r) // 2
            
            total_days = 1
            total_weight = 0

            for w in weights:
                if total_weight + w <= mid:
                    total_weight += w
                else:
                    total_weight = w
                    total_days += 1

            if total_days > days:
                l = mid + 1
            else:
                capacity = mid
                r = mid

        return capacity