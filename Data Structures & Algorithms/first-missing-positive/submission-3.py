class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums): 
            n = nums[i]

            if 1 <= n <= len(nums) and not nums[i] == nums[n - 1]:
                nums[n - 1], nums[i] = nums[i], nums[n - 1]
            else:
                i += 1
        
        for i, n in enumerate(nums):
            if not i + 1 == n:
                return i + 1
        
        return len(nums) + 1