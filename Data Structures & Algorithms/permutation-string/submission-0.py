class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ch1_mapper = {}
        for ch1 in s1:
            ch1_mapper[ch1] = 1 + ch1_mapper.get(ch1, 0)
        
        l = 0
        ch2_mapper = {}
        for r, ch2 in enumerate(s2):
            ch2_mapper[ch2] = 1 + ch2_mapper.get(ch2, 0)

            while r - l + 1 > len(s1):
                ch2_mapper[s2[l]] -= 1

                if ch2_mapper[s2[l]] == 0:
                    del ch2_mapper[s2[l]]

                l += 1

            if ch1_mapper == ch2_mapper: return True
        
        return ch1_mapper == ch2_mapper