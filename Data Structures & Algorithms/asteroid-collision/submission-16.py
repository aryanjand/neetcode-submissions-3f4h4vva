class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue
            
            while stack and 0 < stack[-1] < abs(a):
                stack.pop()
            
            if stack and stack[-1] == abs(a) and a < 0:
                stack.pop()
            elif not stack or a > 0 or stack[-1] < 0:
                stack.append(a)
        
        return stack