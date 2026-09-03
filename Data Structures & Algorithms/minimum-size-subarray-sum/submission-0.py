class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float("inf")

        curr = 0
        l = 0
        for r, n in enumerate(nums):
            curr += n

            while curr >= target:
                minimum = min(r - l + 1, minimum)
                curr -= nums[l]
                l += 1
            
        return 0 if minimum == float("inf") else minimum