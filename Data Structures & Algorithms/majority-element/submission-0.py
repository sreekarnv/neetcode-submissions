class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapper = {}
        for n in nums:
            mapper[n] = 1 + mapper.get(n, 0)

        count = 0
        elem = None
        for k, v in mapper.items():
            if count < v:
                elem = k
                count = v

        return elem
