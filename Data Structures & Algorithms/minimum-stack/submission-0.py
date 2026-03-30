
class MinStack:

    def __init__(self):
        self._stack = []
        self._minStack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._minStack:
            self._minStack.append(val)
        else:
            self._minStack.append(min(self._minStack[-1], val))

    def pop(self) -> None:
        self._stack.pop()
        self._minStack.pop()

    def top(self) -> int:
        return self._stack[-1]        

    def getMin(self) -> int:
        return self._minStack[-1]


# I cannot index the elements
# I cannot use the build in functions for array
# The array needs to dynmic

        
