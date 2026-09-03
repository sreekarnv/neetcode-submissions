class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counters = [0] * 3

        for n in nums:
            counters[n] += 1
        
        n = 0
        for i, c in enumerate(counters):
            for _ in range(c):
                nums[n] = i
                n += 1