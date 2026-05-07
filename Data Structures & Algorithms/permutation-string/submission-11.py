class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for ch1 in s1:
            s1_map[ch1] = 1 + s1_map.get(ch1, 0)

        s2_map = {}
        l = 0
        r = 0

        while r < len(s2):
            ch2 = s2[r]
            s2_map[ch2] = 1 + s2_map.get(ch2, 0)

            if r - l + 1 > len(s1):
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    del s2_map[s2[l]]
                l += 1
            
            if s1_map == s2_map:
                return True

            r += 1

        return False