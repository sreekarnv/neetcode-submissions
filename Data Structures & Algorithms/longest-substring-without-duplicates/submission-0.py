class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()

        l = 0
        for r, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l += 1
            
            longest = max(r - l + 1, longest)
            seen.add(ch)
        
        return longest