class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for i, ch in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < ch:
                j = stack.pop()
                results[j] = i - j
            
            stack.append(i)
        
        return results
        