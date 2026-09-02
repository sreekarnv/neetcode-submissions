class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        longest = min(strs, key=len)

        for s in strs:

            if longest == s: continue

            for i, ch in enumerate(longest):
                for s in strs:
                    if not ch == s[i]: return s[:i]
                
        return longest