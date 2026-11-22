class Node:
    def __init__(self, val: int = 0, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next, self.tail.prev = self.tail, self.head

    def getPrev(self, index: int):
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.getPrev(index)
        return node.next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        self.size += 1
        prev = self.getPrev(index)
        next = prev.next
        node = Node(val, prev, next)
        prev.next = next.prev = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        prev = self.getPrev(index)
        next = prev.next.next
        prev.next = next
        if next:
            next.prev = prev

