class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checker = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for ch in s:
            if not stack or ch not in checker:
                stack.append(ch)
                continue
            
            if not stack[-1] == checker[ch]: return False
            stack.pop()
        
        return len(stack) == 0