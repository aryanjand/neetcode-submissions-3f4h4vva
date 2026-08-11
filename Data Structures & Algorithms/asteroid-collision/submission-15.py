class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0 or not stack or stack[-1] < 0:
                stack.append(a)
                continue

            neg = abs(a)
            while stack and stack[-1] > 0 and neg > stack[-1]:
                stack.pop()
            
            if stack and stack[-1] == neg:
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(a)

        return stack