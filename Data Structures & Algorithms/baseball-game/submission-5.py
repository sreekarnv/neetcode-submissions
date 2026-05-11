class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []

        for ch in operations:
            if ch == "+":
                a, b = result[-1], result[-2]
                result.append(a + b)
            elif ch == "C":
                result.pop()
            elif ch == "D":
                result.append(2 * result[-1])
            else:
                result.append(int(ch))
        
        return sum(result)