class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        tm = {}
        for cht in t:
            tm[cht] = 1 + tm.get(cht, 0)
        need = len(tm)
        have = 0

        minlength = float("inf")
        idxs = None
        sm = {}
        l = 0
        for r, chs in enumerate(s):
            sm[chs] = 1 + sm.get(chs, 0)

            if chs in tm and tm[chs] == sm[chs]:
                have += 1
            
            while have == need:
                if r - l + 1 < minlength:
                    minlength = r - l + 1
                    idxs = l, r

                chl = s[l]

                sm[chl] -= 1

                if chl in tm and tm[chl] > sm[chl]:
                    have -= 1

                if sm[chl] == 0:
                    del sm[chl]

                l += 1
            
        return "" if idxs == None else s[idxs[0]:idxs[1] + 1]

