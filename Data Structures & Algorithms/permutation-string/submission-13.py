class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1m = {}
        for ch1 in s1:
            s1m[ch1] = 1 + s1m.get(ch1, 0)
        
        s2m = {}
        l = r = 0

        while r < len(s2):
            ch2 = s2[r]
            s2m[ch2] = 1 + s2m.get(ch2, 0)

            if r - l + 1 > len(s1):
                ch3 = s2[l]
                s2m[ch3] -= 1
                if s2m[ch3] == 0:
                    del s2m[ch3]
                l += 1

            if s1m == s2m:
                return True
            
            r += 1
        
        return False