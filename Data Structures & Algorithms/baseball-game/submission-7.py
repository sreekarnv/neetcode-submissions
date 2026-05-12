class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []

        for ch in operations:
            if ch == "+":
                results.append(results[-1] + results[-2])
            elif ch == "C":
                results.pop()
            elif ch == "D":
                results.append(2 * results[-1])
            else:
                results.append(int(ch))
        
        return sum(results)