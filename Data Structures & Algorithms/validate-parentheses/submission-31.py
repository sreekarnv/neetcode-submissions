class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []

        for n in s:
            if not stack or n not in mapper:
                stack.append(n)
                continue

            if stack[-1] != mapper[n]:
                return False
            stack.pop()
        
        return len(stack) == 0
