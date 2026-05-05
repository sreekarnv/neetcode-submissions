class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0

        curr_sum = 0
        min_len = float("infinity")

        while r < len(nums):
            curr_sum += nums[r]

            while curr_sum >= target:
                curr_sum -= nums[l]
                min_len = min(min_len, r - l + 1)
                l += 1

            r += 1
        
        return 0 if min_len == float("infinity") else min_len