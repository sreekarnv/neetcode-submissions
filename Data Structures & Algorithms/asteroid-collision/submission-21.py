class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        results = []
        
        for i, a in enumerate(asteroids):
            is_destroyed = False

            while results and a < 0 and results[-1] > 0:
                from_left = abs(results[-1])
                from_right = abs(a)

                if from_left > from_right:
                    is_destroyed = True
                    break
                elif from_left < from_right:
                    results.pop()
                else:
                    results.pop()
                    is_destroyed = True
                    break

            if not is_destroyed:
                results.append(a)
            
        return results