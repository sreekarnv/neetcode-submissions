class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        result = []

        for t in s:
            if t not in mapper:
                result.append(t)
                continue
            
            if result and mapper[t] == result[-1]:
                result.pop()
            else:
                result.append(t)
        
        return len(result) == 0
        
