class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []

        for t in tokens:
            if t == "+":
                a, b = result.pop(), result.pop()
                result.append(a + b)
            elif t == "-":
                a, b = result.pop(), result.pop()
                result.append(b - a)
            elif t == "/":
                a, b = result.pop(), result.pop()
                result.append(int(b / a))
            elif t == "*":
                a, b = result.pop(), result.pop()
                result.append(b * a)
            else:
                result.append(int(t))

        return result[0]
        