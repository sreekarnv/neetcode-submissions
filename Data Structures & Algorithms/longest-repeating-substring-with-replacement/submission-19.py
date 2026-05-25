class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapper = {}
        maxF = 0
        l = 0
        longest = 0

        for r, ch in enumerate(s):
            mapper[ch] = 1 + mapper.get(ch, 0)
            maxF = max(maxF, mapper[ch])

            if (r - l + 1) - maxF > k:
                mapper[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest