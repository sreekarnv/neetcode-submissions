class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_sum = float("inf")

        count = 0

        l = 0
        for r, n in enumerate(nums):
            count += n

            while count >= target:
                min_sum = min(r - l + 1, min_sum)
                count -= nums[l]
                l += 1
            
        return 0 if min_sum == float("inf") else min_sum