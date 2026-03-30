from collections import deque

class MyStack:

    def __init__(self):
        self._queue = deque()

    def push(self, x: int) -> None:
        self._queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self._queue) - 1):
            element = self._queue.popleft()
            self._queue.append(element)
        res = self._queue.popleft()
        return res

        

    def top(self) -> int:
        for _ in range(len(self._queue) - 1):
            element = self._queue.popleft()
            self._queue.append(element)
        res = self._queue.popleft()
        self._queue.append(res)
        return res
        

    def empty(self) -> bool:
        return len(self._queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()