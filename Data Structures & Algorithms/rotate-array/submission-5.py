class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        results = [0] * len(nums)
        
        for i, n in enumerate(nums):
            idx = (i + k) % len(nums)
            results[idx] = n
        
        nums[:] = results
        