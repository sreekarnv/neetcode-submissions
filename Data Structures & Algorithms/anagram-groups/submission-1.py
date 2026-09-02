class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for s in strs:
            sk = [0] * 26
            for ch in s:
                sk[ord(ch) - ord('a')] += 1
            sk = tuple(sk)

            if sk not in results:
                results[sk] = []
            
            results[sk].append(s)
        
        return list(results.values())