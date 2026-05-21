class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        results = []

        for i in range(len(asteroids)):
            a = asteroids[i]
            isDone = False

            while results and results[-1] > 0 and a < 0:
                if abs(results[-1]) < abs(a):
                    results.pop()
                elif abs(results[-1]) == abs(a):
                    results.pop()
                    isDone = True   
                    break
                else:
                    isDone = True   
                    break

            if not isDone:
                results.append(a)
        
        return results