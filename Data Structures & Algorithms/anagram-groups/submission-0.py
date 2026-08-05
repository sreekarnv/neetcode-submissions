class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            chars = [0] * 26

            for ch in s:
                chars[ord(ch) - ord('a')] += 1
            
            chars = tuple(chars)

            if chars not in result:
                result[chars] = []
            
            result[chars].append(s)
        
        return list(result.values())