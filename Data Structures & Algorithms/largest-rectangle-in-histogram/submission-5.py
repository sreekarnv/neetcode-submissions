class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0

        for i, h in enumerate(heights):
            curr = i
            while stack and stack[-1][1] > h:
                j, val = stack.pop()
                largest = max((i - j) * val, largest)
                curr = j
            
            stack.append((curr, h))
        
        for i, h in stack:
            w = len(heights) - i
            largest = max(h * w, largest)

        return largest