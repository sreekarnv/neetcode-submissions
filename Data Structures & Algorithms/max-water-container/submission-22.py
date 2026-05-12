class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            h = min(heights[r], heights[l]) 
            w = r - l
            area = max(h * w, area)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return area