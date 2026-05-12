class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapper = {}
        maxF = 0
        l = 0
        longest = 0

        for r, ch in enumerate(s):
            mapper[ch] = 1 + mapper.get(ch, 0)

            maxF = max(maxF, mapper[ch])
            ws = r - l + 1

            if ws - maxF > k:
                mapper[s[l]] -= 1
                if mapper[s[l]] == 0:
                    del mapper[s[l]]
                l += 1
            else:
                longest = max(longest, r - l + 1)
        
        return longest