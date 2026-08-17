class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x

        l = 0
        r = x
        res = x

        while l <= r:
            mid = (l + r) // 2

            val = mid * mid

            if val > x:
                r = mid - 1
            elif val < x:
                res = mid
                l = mid + 1
            else:
                res = mid
                break
        
        return res