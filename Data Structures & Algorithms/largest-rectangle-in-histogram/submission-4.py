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

        for j, h in stack:
            largest = max((len(heights) - j) * h, largest)

        return largest
