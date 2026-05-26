class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for r, a in enumerate(asteroids):
            is_destroyed = False
    
            while stack and a < 0 and stack[-1] > 0:
                left = abs(stack[-1])
                right = abs(a)
                if left > right:
                    is_destroyed = True
                    break
                elif left < right:
                    stack.pop()
                else:
                    stack.pop()
                    is_destroyed = True
                    break

            if not is_destroyed:
                stack.append(asteroids[r])
        
        return stack