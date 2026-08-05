class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        counters = []
        for i, v in freq.items():
            counters.append((v, i))
        counters.sort(reverse=True, key=lambda x: (-x[0], x[1]))

        results = []
        while len(results) < k:
            results.append(counters.pop()[1])
        
        return results