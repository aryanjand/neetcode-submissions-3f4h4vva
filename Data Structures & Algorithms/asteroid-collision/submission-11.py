class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for j in range(len(asteroids)):
            asteroid = asteroids[j]
            while stack and asteroid < 0 < stack[-1]:
                pos, neg = stack.pop(), abs(asteroid)
                if pos == neg:
                    asteroid = 0
                    break
                elif pos > neg:
                    asteroid = pos
            if asteroid != 0:
                stack.append(asteroid)
                
        return stack