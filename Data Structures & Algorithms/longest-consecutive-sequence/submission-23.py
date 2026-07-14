class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
    
        longest = 0
    
        for i, n in enumerate(nums):
            if n - 1 not in nums:
                c = 0
                while c + n in nums:
                    c += 1
                longest = max(longest, c)
            
        return longest