class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        results = []

        for ch in tokens:
            if ch == "+":
                a, b = results.pop(), results.pop()
                results.append(b + a)
            elif ch == "-":
                a, b = results.pop(), results.pop()
                results.append(b - a)
            elif ch == "*":
                a, b = results.pop(), results.pop()
                results.append(b * a)
            elif ch == "/":
                a, b = results.pop(), results.pop()
                results.append(int(b / a))
            else:
                results.append(int(ch))
        
        return results[-1]