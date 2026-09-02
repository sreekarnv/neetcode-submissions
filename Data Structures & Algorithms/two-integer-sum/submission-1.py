class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for i, n in enumerate(nums):
            m = target - n

            if m in counter: return [counter[m], i]

            counter[n] = i
        