class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for i, n in enumerate(nums):
            m = target - n

            if m in mapper:
                return [mapper[m], i]

            mapper[n] = i
