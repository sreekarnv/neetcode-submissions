class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        
        for o in operations:
            if o == "+":
                results.append(results[-1] + results[-2])
            elif o == "C":
                results.pop()
            elif o == "D":
                results.append(2 * results[-1])
            else:
                results.append(int(o))
        
        return sum(results)