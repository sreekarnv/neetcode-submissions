class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_map = {}
        for ch in t:
            t_map[ch] = 1 + t_map.get(ch, 0)
        
        need = len(t_map)
        have = 0
        
        min_len = float("inf")
        idxs = None

        l = 0
        r = 0
        s_map = {}

        while r < len(s):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)

            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < min_len:
                    idxs = l, r
                    min_len = r - l + 1
                
                if s[l] in s_map:
                    s_map[s[l]] -= 1

                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1

                l += 1

            r += 1
        
        return "" if min_len == float("inf") else s[idxs[0]:idxs[1] + 1]