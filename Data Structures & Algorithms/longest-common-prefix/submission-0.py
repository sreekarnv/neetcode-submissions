class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        
        ref = strs[0]

        for i in range(len(ref)):
            ch = ref[i]

            for j in range(1, len(strs)):
                s = strs[j]

                if i > len(s) - 1 or not s[i] == ch:
                    return ref[:i]
        
        return ref