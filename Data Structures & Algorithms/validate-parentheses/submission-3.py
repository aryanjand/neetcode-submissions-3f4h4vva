class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '{': '}','[': ']'}

        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            else:
                if not stack or bracket != brackets[stack[-1]]:
                    return False
                stack.pop()
        
        return len(stack) == 0