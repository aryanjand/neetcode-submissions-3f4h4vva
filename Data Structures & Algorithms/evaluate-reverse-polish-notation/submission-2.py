class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case '+':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    stack.append(operand1 + operand2)
                    continue
                case '-':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    stack.append(operand1 - operand2)
                    continue
                case '*':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    stack.append(operand1 * operand2)
                    continue
                case '/':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    stack.append(int(operand1 / operand2))
                    continue
            stack.append(int(t))
        
        return stack.pop()
