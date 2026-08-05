class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq = {}
        max_freq = 0

        l = 0
        for r, ch in enumerate(s):
            freq[ch] = 1 + freq.get(ch, 0)
            max_freq = max(freq[ch], max_freq)

            if r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                
                if freq[s[l]] == 0:
                    del freq[s[l]]
                
                l += 1

            longest = max(r - l + 1, longest)

        return longest
