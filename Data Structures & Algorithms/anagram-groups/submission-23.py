class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for s in strs:
            curr = [0] * 26

            for ch in s:
                curr[ord(ch) - ord('a')] += 1
            curr = tuple(curr)

            if curr not in results:
                results[curr] = []

            results[curr].append(s)
        
        return list(results.values())