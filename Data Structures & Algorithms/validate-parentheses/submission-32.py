class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        results = []

        for ch in s:
            if ch not in mapper or not results:
                results.append(ch)
                continue
            
            if results[-1] != mapper[ch]:
                return False
            
            results.pop()
        
        return len(results) == 0
