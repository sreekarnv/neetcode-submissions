class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        i = 0
        while i < len(nums):
            n = nums[i]
            if not n - 1 in nums:
                c = 1
                next_num = n + 1
                while next_num in nums:
                    c += 1
                    next_num += 1
                    
                longest = max(longest, c)
            
            i += 1
        
        return longest