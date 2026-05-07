class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float("inf")

        l = 0
        r = 0

        count = 0

        while r < len(nums):
            count += nums[r]

            while count >= target:
                minimum = min(minimum, r - l + 1)
                count -= nums[l]
                l += 1

            r += 1
        
        return 0 if minimum == float("inf") else minimum