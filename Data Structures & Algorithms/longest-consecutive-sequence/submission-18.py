class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        i = 0
        while i < len(nums):
            n = nums[i]
            if n - 1 not in nums_set:
                c = 0
                while n + c in nums_set:
                    c += 1
                longest = max(longest, c)
            i += 1

        return longest