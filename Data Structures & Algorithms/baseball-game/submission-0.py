class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ch in operations:
            if ch == "+":
                a, b = stack[-1], stack[-2]
                stack.append(a + b)
            elif ch == "C":
                stack.pop()
            elif ch == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(ch))
        
        return sum(stack)