class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        results = []

        for t in tokens:
            if t == "+":
                a, b = results.pop(), results.pop()
                results.append(a + b)
            elif t == "-":
                a, b = results.pop(), results.pop()
                results.append(b - a)
            elif t == "/":
                a, b = results.pop(), results.pop()
                results.append(int(b / a))
            elif t == "*":
                a, b = results.pop(), results.pop()
                results.append(b * a)
            else:
                results.append(int(t))
        
        return results[0]