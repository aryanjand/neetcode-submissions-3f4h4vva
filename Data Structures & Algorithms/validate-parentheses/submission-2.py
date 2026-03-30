class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '{': '}','[': ']'}

        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                close = brackets[stack[-1]]
                if close != bracket:
                    return False
                stack.pop()
        
        return len(stack) == 0