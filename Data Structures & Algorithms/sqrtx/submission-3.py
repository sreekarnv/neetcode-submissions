class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        l = 0
        r = x - 1
        answer = 0

        while l <= r:
            mid = (l + r) // 2
            curr = mid * mid
            
            if curr == x:
                return mid
            
            if curr > x:
                r = mid - 1
            else:
                answer = mid
                l = mid + 1
        
        return answer