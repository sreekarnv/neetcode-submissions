class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if not ch == "]":
                stack.append(ch)
                continue
            
            curr = ""
            while stack and not stack[-1] == "[":
                curr = stack.pop() + curr
            stack.pop()

            num = ""
            while stack and stack[-1].isnumeric():
                num = stack.pop() + num
            num = int(num)

            stack.append(num * curr)
        
        return "".join(stack)