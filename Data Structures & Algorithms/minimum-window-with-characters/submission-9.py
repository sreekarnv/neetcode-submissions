class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}
        for t1 in t:
            tmap[t1] = 1 + tmap.get(t1, 0)
        need = len(tmap)

        smap = {}
        l = 0
        r = 0
        idxs = None
        min_len = float("inf")
        have = 0

        while r < len(s):
            s1 = s[r]
            smap[s1] = 1 + smap.get(s1, 0)

            if s1 in tmap and smap[s1] == tmap[s1]:
                have += 1
            
            while have == need:
                if min_len > r - l + 1:
                    min_len = r - l + 1
                    idxs = l, r
                
                s2 = s[l]
                if s2 in tmap and tmap[s2] == smap[s2]:
                    have -= 1
                
                smap[s2] -= 1

                l += 1
            
            r += 1
        
        if min_len == float("inf"):
            return ""
        
        l, r = idxs
        return s[l:r + 1]