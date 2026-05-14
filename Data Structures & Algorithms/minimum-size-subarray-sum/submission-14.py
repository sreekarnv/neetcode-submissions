class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        curr = 0

        l = 0
        for r, n in enumerate(nums):
            curr += n

            while curr >= target:
                min_len = min(min_len, r - l + 1)
                curr -= nums[l]
                l += 1
            
        return 0 if min_len == float("inf") else min_len