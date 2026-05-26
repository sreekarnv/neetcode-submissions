class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        results = []

        l = 0
        for r, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            while q and r - l + 1 == k:
                results.append(nums[q[0]])
                l += 1

        return results