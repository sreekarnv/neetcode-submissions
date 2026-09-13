class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
                
        ch_map = {}

        for ch in s:
            ch_map[ch] = 1 + ch_map.get(ch, 0)
        
        for ch in t:
            if ch not in ch_map:
                return False
            
            ch_map[ch] -= 1
            if ch_map[ch] == 0:
                del ch_map[ch]
        
        return len(ch_map) == 0
        