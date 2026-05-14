class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        postfix = 1

        i = 0
        while i < len(nums):
            result[i] = prefix
            prefix *= nums[i]
            i += 1

        j = len(nums) - 1
        while j >= 0:
            result[j] *= postfix
            postfix *= nums[j]
            j -= 1
        
        return result