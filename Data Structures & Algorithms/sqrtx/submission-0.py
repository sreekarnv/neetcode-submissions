class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        
        val = 0

        for i in range(x):
            if i * i > x: break

            val = i
        
        return val