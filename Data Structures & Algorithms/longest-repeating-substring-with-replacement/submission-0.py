class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapper = {}
        longest = 0
        freq = 0
        l = 0

        for r, ch in enumerate(s):
            mapper[ch] = 1 + mapper.get(ch, 0)
            freq = max(freq, mapper[ch])
            
            if r - l + 1 - freq > k:
                mapper[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest 