class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for char in operations:
            if char == '+':
                stack.append(stack[-2] + stack[-1])
            elif char == 'D':
                stack.append(stack[-1] * 2)
            elif char == 'C':
                stack.pop()
            else:
                stack.append(int(char))

        return sum(stack)