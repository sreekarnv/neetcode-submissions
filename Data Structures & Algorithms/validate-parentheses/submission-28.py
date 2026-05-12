class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        results = []

        for ch in s:
            if not results or ch not in mapper:
                results.append(ch)
            else:
                if results[-1] != mapper[ch]:
                    return False
                results.pop()
        
        return len(results) == 0