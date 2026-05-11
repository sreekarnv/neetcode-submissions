class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        mapper = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for ch in s:
            if ch not in mapper:
                result.append(ch)
            else:
                if not result or mapper[ch] != result[-1]:
                    return False
                result.pop()
        
        return len(result) == 0