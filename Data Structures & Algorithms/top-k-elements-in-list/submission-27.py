class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        for n in nums:
            mapper[n] = 1 + mapper.get(n, 0)
        
        counters = []
        for n, v in mapper.items():
            counters.append((v, n))
        counters.sort(reverse=True, key=lambda x: (-x[0], x[1]))

        results = []
        while len(results) < k:
            results.append(
                counters.pop()[1]
            )
        
        return results