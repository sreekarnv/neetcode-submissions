class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapper = {}
        maxf_ch = 0

        longest = 0

        l = 0
        for r, ch in enumerate(s):
            mapper[ch] = 1 + mapper.get(ch, 0)
            maxf_ch = max(maxf_ch, mapper[ch])

            if (r - l + 1) - maxf_ch > k:
                mapper[s[l]] -= 1
                if mapper[s[l]] == 0:
                    del mapper[s[l]]
                
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest