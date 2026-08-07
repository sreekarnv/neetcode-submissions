class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i, a in enumerate(asteroids):
            is_destroyed = False

            while a < 0 and stack and stack[-1] > 0:
                ltr = abs(stack[-1])
                rtl = abs(a)

                if ltr > rtl:
                    is_destroyed = True
                    break
                elif ltr < rtl:
                    stack.pop()
                else:
                    stack.pop()
                    is_destroyed = True
                    break
            
            if not is_destroyed:
                stack.append(a)

        return stack