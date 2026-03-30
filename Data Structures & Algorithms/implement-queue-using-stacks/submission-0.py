from collections import deque

class MyQueue:

    def __init__(self):
        self._stack = deque()
        self._tempStack = deque()
        

    def push(self, x: int) -> None:
        self._stack.append(x)
        
    def pop(self) -> int:
        for _ in range(len(self._stack) - 1):
            element = self._stack.pop()
            self._tempStack.append(element)
        res = self._stack.pop()
        for _ in range(len(self._tempStack)):
            element = self._tempStack.pop()
            self._stack.append(element)
        return res
        

    def peek(self) -> int:
        for _ in range(len(self._stack) - 1):
            element = self._stack.pop()
            self._tempStack.append(element)
        res = self._stack.pop()
        self._tempStack.append(res)
        for _ in range(len(self._tempStack)):
            element = self._tempStack.pop()
            self._stack.append(element)
        return res

    def empty(self) -> bool:
        return len(self._stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()