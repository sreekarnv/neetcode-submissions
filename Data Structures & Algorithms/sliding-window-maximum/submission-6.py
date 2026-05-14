class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        r = 0
        results = []

        while r < len(nums):
            n = nums[r]

            while q and nums[q[-1]] < n:
                q.pop()
            
            q.append(r)

            while q[0] < l:
                q.popleft()
            
            while r - l + 1 == k:
                results.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return results