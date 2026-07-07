class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if not m[0] <= target <= m[-1]:
                continue
            
            l = 0
            r = len(m) - 1

            while l <= r:
                mid = (l + r) // 2

                if m[mid] == target:
                    return True
                elif m[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False