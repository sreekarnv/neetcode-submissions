class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for n in nums_set:
            if n - 1 not in nums_set:
                count = 0
                while count + n in nums_set:
                    count += 1
                
                longest = max(count, longest)

        return longest