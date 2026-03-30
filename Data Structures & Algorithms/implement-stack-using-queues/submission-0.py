class MyStack:

    def __init__(self):
        self._queue = []
        self._tempQueue = []

    def push(self, x: int) -> None:
        self._queue.append(x)

    def pop(self) -> int:
        for index in range(len(self._queue) - 1):
            element = self._queue.pop(0)
            self._tempQueue.append(element)
        res = self._queue.pop(0)
        self._queue = self._tempQueue.copy()
        self._tempQueue = []
        return res

        

    def top(self) -> int:
        for index in range(len(self._queue) - 1):
            element = self._queue.pop(0)
            self._tempQueue.append(element)
        res = self._queue.pop(0)
        self._tempQueue.append(res)
        self._queue = self._tempQueue.copy()
        self._tempQueue = []
        return res
        

    def empty(self) -> bool:
        return len(self._queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()