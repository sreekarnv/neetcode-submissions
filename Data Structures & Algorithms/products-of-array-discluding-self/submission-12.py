class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)

        prefix = 1

        for i, n in enumerate(nums):
            results[i] *= prefix
            prefix *= n
        
        postfix = 1
        i = len(nums) - 1
        while i >= 0:
            results[i] *= postfix
            postfix *= nums[i]

            i -= 1
        
        return results