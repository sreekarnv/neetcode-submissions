class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapper = {}

        for ch in s:
            mapper[ch] = 1 + mapper.get(ch, 0)
        
        for ch in t:
            if ch not in mapper:
                return False
            
            mapper[ch] -= 1

            if mapper[ch] == 0:
                del mapper[ch]
        
        return len(mapper) == 0