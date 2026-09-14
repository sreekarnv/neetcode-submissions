class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []

        for ch in s:
            if not stack or ch not in mapper:
                stack.append(ch)
                continue
            
            if not stack[-1] == mapper[ch]:
                return False
            
            stack.pop()
        
        return len(stack) == 0