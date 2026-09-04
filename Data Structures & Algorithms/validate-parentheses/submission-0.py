class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []

        for ch in s:
            if not stack or ch not in mapper:
                stack.append(ch)
                continue
            
            if not mapper[ch] == stack[-1]:
                return False
            
            stack.pop()
        
        return len(stack) == 0