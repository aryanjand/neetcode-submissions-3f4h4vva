class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        i = 0

        while cur and i < index:
            cur = cur.next
            i += 1

        return cur.value if cur else -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

        if not self.tail:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = Node(val)

        if not self.head:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True

        prev = None
        cur = self.head
        i = 0

        while cur and i < index:
            prev = cur
            cur = cur.next
            i += 1

        if not cur:
            return False

        prev.next = cur.next
        if cur == self.tail:
            self.tail = prev

        return True

    def getValues(self) -> list[int]:
        res = []
        cur = self.head

        while cur:
            res.append(cur.value)
            cur = cur.next

        return res
