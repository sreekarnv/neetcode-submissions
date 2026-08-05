class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minsize = float("inf")
        curr = 0

        l = 0
        for r, n in enumerate(nums):
            curr += n

            while curr >= target:
                minsize = min(minsize, r - l + 1)
                curr -= nums[l]
                l += 1
            
        return 0 if minsize == float("inf") else minsize