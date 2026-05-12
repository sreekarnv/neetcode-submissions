class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tmap = {}
        for cht in t:
            tmap[cht] = 1 + tmap.get(cht, 0)
        need = len(tmap)
        have = 0
        
        mapper = {}
        idxs = None
        min_len = float("inf")

        r = 0
        l = 0

        while r < len(s):
            ch = s[r]
            mapper[ch] = 1 + mapper.get(ch, 0)

            if ch in tmap and mapper[ch] == tmap[ch]:
                have += 1
            
            while have == need:
                if min_len > r - l + 1:
                    min_len = r - l + 1
                    idxs = (l, r)

                ch2 = s[l]
                mapper[ch2] -= 1
                   
                if ch2 in tmap and mapper[ch2] < tmap[ch2]:
                    have -= 1

                l += 1                

            r += 1

        return "" if min_len == float("inf") else s[idxs[0]:idxs[1] + 1]