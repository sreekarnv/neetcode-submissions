class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ma in matrix:
            l = 0
            r = len(ma) - 1

            while l <= r:
                m = (l + r) // 2

                if ma[m] == target:
                    return True
                
                if ma[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        
        return False