class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                else:
                    while stack:
                        right, left = stack.pop(), abs(asteroid)

                        if right > left:
                            stack.append(right)
                            break
                        elif right == left:
                            break
                        elif not stack or stack[-1] < 0:
                            stack.append(asteroid)
                            break
        
        return stack