class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in nums_set:
                c = 1
                while c + n in nums_set:
                    c += 1
                
                longest = max(c, longest)
        
        return longest