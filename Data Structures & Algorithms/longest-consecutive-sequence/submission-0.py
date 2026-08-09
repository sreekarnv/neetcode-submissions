class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for n in nums_set:
            if n - 1 not in nums_set:
                c = 0

                while c + n in nums_set:
                    c += 1
                
                longest = max(c, longest)   

        return longest