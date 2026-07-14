class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        
        for s in strs:
            curr = [0] * 26

            for ch in s:
                curr[ord(ch) - ord('a')] += 1
            
            curr = tuple(curr)
            if curr not in mapper:
                mapper[curr] = []
            
            mapper[curr].append(s)
        

        return list(mapper.values())