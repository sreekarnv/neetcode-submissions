class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _nums = set(nums)
        max_val = 0

        for n in _nums:
            if not n - 1 in _nums:
                seq = 0
                while n + seq in nums:
                    seq += 1
                max_val = max(max_val, seq)
        
        return max_val