class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        stack = deque()
        l = 0
        
        for r in range(len(nums)):
            while stack and nums[stack[-1]] < nums[r]:
                stack.pop()
            
            stack.append(r)

            while stack[0] < l:
                stack.popleft()
            
            while r - l + 1 == k:
                results.append(nums[stack[0]])
                l += 1


        return results