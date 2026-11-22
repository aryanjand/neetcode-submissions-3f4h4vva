class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def getPrev(self, index: int):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self.getPrev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        prev = self.getPrev(index)
        next = prev.next

        node = Node(val, prev, next)

        prev.next = next.prev = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:
            return

        prev = self.getPrev(index)
        cur = prev.next
        next = cur.next

        prev.next = next
        next.prev = prev

        self.size -= 1
