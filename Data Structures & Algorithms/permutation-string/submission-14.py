class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1m = {}
        for ch1 in s1:
            s1m[ch1] = 1 + s1m.get(ch1, 0)
        
        s2m = {}
        l = 0
        for r, ch2 in enumerate(s2):
            s2m[ch2] = 1 + s2m.get(ch2, 0)

            if r - l + 1 > len(s1):
                s2m[s2[l]] -= 1
                if s2m[s2[l]] == 0:
                    del s2m[s2[l]]
                l += 1

            if s1m == s2m:
                return True
        
        return False