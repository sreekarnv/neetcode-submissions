class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums)

        if n < 0: n = 1

        for i in range(1, n + 2):
            if i not in nums_set:
                return i
        
        return n + 1