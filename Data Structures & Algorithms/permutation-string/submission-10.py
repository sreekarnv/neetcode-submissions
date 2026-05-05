class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for ch1 in s1:
            if ch1 not in s1_map:
                s1_map[ch1] = 0
            s1_map[ch1] += 1
        
        l = 0
        s2_map = {}
        for r, n in enumerate(s2):
            if n not in s2_map:
                s2_map[n] = 0
            s2_map[n] += 1
     
            if sum(s2_map.values()) > len(s1):
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    del s2_map[s2[l]]
                l += 1
            
            if s2_map == s1_map:
                return True
        
        return False