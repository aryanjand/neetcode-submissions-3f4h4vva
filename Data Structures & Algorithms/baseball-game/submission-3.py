class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for char in operations:
            if char == '+':
                operand2 = stack.pop()
                operand1 = stack.pop()
                value = operand1 + operand2
                stack.append(operand1)
                stack.append(operand2)
                stack.append(value)
            elif char == 'D':
                operand1 = stack.pop()
                value = operand1 * 2
                stack.append(operand1)
                stack.append(value)
            elif char == 'C':
                stack.pop()
            else:
                stack.append(int(char))
        return sum(stack)