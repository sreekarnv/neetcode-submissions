class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        for n in nums:
            mapper[n] = 1 + mapper.get(n, 0)
        
        counts = []
        for _k, v in mapper.items():
            counts.append((v, _k))
        counts.sort(key=lambda x: (x[0], -x[1]))

        results = []
        while counts and len(results) < k:
            results.append(counts.pop()[1])
        
        return results