class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minval = float("inf")
        curr = 0
        l = 0
        
        for r, n in enumerate(nums):
            curr += n

            while curr >= target:
                minval = min(minval, r - l + 1)
                curr -= nums[l]
                l += 1
            
        return 0 if minval == float("inf") else minval
