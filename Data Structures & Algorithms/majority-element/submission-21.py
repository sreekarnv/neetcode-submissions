class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums) // 2

        mapper = {}
        for n in nums:
            mapper[n] = 1 + mapper.get(n, 0)
        
        counters = []
        for k, v in mapper.items():
            if v >= m:
                counters.append((v, k))
        counters.sort()

        return counters.pop()[1]