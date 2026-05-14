class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapper = {}
        longest = 0

        l = 0
        maxF = 0
        r = 0
        
        while r < len(s):
            mapper[s[r]] = 1 + mapper.get(s[r], 0)
            maxF = max(maxF, mapper[s[r]])

            while (r - l + 1) - maxF > k:
                mapper[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest
