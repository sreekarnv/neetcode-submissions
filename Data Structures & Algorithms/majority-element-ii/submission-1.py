class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapper = defaultdict(int)
        for n in nums:
            mapper[n] += 1
        
        counters = []
        for k, v in mapper.items():
            counters.append((v, k))
        counters.sort()

        result = []
        for i in range(len(counters) - 1, -1, -1):
            k, v = counters.pop()
            if k > int(len(nums) / 3):
                result.append(v)
        
        return result