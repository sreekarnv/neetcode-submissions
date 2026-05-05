class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = {}
        long_str = 0

        l = 0

        for r, n in enumerate(s):
            if n not in f:
                f[n] = 0
            f[n] += 1
        
            maxF = max(f.values())
            ws = r - l + 1

            if ws - maxF <= k:
                long_str = max(long_str, r - l + 1)
            else:
                f[s[l]] -= 1
                if f[s[l]] == 0:
                    del f[s[l]]
                l += 1
        
        return long_str