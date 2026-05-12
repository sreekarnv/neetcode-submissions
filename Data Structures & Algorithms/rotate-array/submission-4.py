class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * len(nums)

        for i, n in enumerate(nums):
            res[(i + k) % len(nums)] = n

        nums[:] = res           
