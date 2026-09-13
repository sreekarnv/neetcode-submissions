class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for s in strs:
            chs = [0] * 26
            
            for ch in s:
                chs[ord(ch) - ord('a')] += 1
            
            chs = tuple(chs)

            if chs not in results:
                results[chs] = []
            
            results[chs].append(s)
        
        return list(results.values())