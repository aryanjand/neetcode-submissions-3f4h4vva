class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        self._capacity = 19_997
        self._arr = [Node(None) for _ in range(self._capacity)]
        
    def _hash(self, key: int) -> int:
        return key % self._capacity

    def add(self, key: int) -> None:
        node = self._arr[self._hash(key)]
        while node.next:
            node = node.next
            if node.val == key:
                return None
        node.next = Node(key)


    def remove(self, key: int) -> None:
        node = self._arr[self._hash(key)]
        while node.next and node.next.val != key:
            node = node.next        
        node.next = node.next.next if node.next else None

    def contains(self, key: int) -> bool:
        node = self._arr[self._hash(key)].next
        while node:
            if node.val == key:
                return True
            node = node.next
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)