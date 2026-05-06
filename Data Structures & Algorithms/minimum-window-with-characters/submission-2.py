class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tmap = {}
        for ti in t:
            tmap[ti] = 1 + tmap.get(ti, 0)
        
        need = len(tmap)
        have = 0
        
        smap = {}

        l = 0
        r = 0

        min_idx = None
        min_len = float("infinity")

        while r < len(s):
            curr = s[r]
            smap[curr] = 1 + smap.get(curr, 0)

            if curr in tmap and smap[curr] == tmap[curr]:
                have += 1

            while need == have:
                if r - l + 1 < min_len:
                    min_idx = (l, r)
                    min_len = r - l + 1

                if s[l] in smap:
                    smap[s[l]] -= 1
                    
                if s[l] in tmap and tmap[s[l]] > smap[s[l]]:
                    have -= 1

                l += 1

            r += 1

        return "" if min_len == float("inf") else s[min_idx[0]:min_idx[1] + 1]
            
