class DynamicArray:
    
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._arr = [0] * capacity
        self._size = 0

    def get(self, i: int) -> int:
        return self._arr[i]


    def set(self, i: int, n: int) -> None:
        self._arr[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self._arr[self._size] = n
        self._size += 1


    def popback(self) -> int:
        self._size -= 1
        res = self._arr[self._size]
        return res

    def resize(self) -> None:
        self._capacity = self._capacity * 2
        newArr = [0] * self._capacity

        for i in range(len(self._arr)):
            newArr[i] = self._arr[i]
        self._arr = newArr


    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity