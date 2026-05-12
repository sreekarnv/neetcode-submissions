class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            curr = i
            while stack and stack[-1][1] > heights[i]:
                j, val = stack.pop()
                max_area = max((i - j) * val, max_area)
                curr = j

            stack.append([curr, h]) 
        
        for j, val in stack:
            max_area = max(max_area, (len(heights) - j) * val)
        
        return max_area