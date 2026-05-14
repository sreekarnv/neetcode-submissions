class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapper = {}
        l = 0
        r = 0
        longest = 0
        maxF = 0

        while r < len(s):
            mapper[s[r]] = 1 + mapper.get(s[r], 0)
            maxF = max(mapper[s[r]], maxF)
            ws = r - l + 1

            if ws - maxF > k:
                mapper[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest
