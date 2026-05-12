class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}
        
        for t1 in t:
            tmap[t1] = 1 + tmap.get(t1, 0)
        
        need = len(tmap)
        have = 0

        l = 0
        r = 0

        smap = {}
        idxs = None
        min_len = float("inf")

        while r < len(s):
            ch = s[r]
            smap[ch] = 1 + smap.get(ch, 0)

            if ch in tmap and tmap[ch] == smap[ch]:
                have += 1

            while have == need:
                ch2 = s[l]
                if min_len > r - l + 1:
                    min_len = r - l + 1
                    idxs = l, r
                
                smap[ch2] -= 1

                if ch2 in tmap and tmap[ch2] > smap[ch2]:
                    have -= 1
            
                l += 1

            r += 1

        return "" if min_len == float("inf") else s[idxs[0]:idxs[1] + 1]